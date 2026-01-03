class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def is_palindrome(left: int, right: int):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def dfs(start: int, current_partition: list):
            if start == len(s):
                result.append(current_partition[:])
                return
            
            for end in range(start, len(s)):
                if is_palindrome(start, end):
                    current_partition.append(s[start:end+1])
                    dfs(end+1, current_partition)
                    current_partition.pop()

        dfs(0, [])
        return result
