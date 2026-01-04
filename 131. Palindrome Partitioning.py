class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        n = len(s)

        # Precompute palindrome table
        is_palindrome = [[False] * n for _ in range(n)]
        for left in range(n - 1, -1, -1):
            for right in range(left, n):
                if (s[left] == s[right] and 
                    (right - left <= 2 or is_palindrome[left + 1][right - 1])):
                    is_palindrome[left][right] = True

        def dfs(start: int, current_partition: list):
            if start == n:
                result.append(current_partition[:])
                return
            
            for end in range(start, n):
                if is_palindrome[start][end]:
                    current_partition.append(s[start:end + 1])
                    dfs(end + 1, current_partition)
                    current_partition.pop()

        dfs(0, [])
        return result
