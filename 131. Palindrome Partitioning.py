class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def is_palindrome(left: int, right: int):
            while left < right:
                if s[left] != s[right]:
                    return False
                left, right = left + 1, right - 1
            return True

        def dfs(i: int, current_partition: list):
            if i == len(s):
                result.append(current_partition[:])
                return
            
            for j in range(i, len(s)):
                if is_palindrome(i, j):
                    current_partition.append(s[i:j+1])
                    dfs(j+1, current_partition)
                    current_partition.pop()

        dfs(0, [])
        return result
