class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        for i in range(len(s)):
            left = right = i
            result += 1

            while right + 1 < len(s) and s[right + 1] == s[i]:
                right += 1
                result += 1

            while left - 1 >= 0 and right + 1 < len(s) and s[left - 1] == s[right + 1]:
                left -= 1
                right += 1
                result += 1

        return result
