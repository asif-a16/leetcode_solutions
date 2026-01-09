class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        for i in range(len(s)):
            left = right = i

            while right + 1 < len(s) and s[right + 1] == s[i]:
                right += 1

            while left - 1 >= 0 and right + 1 < len(s) and s[left - 1] == s[right + 1]:
                left -= 1
                right += 1

            if right + 1 - left > len(res):
                res = s[left:right + 1]

        return res
