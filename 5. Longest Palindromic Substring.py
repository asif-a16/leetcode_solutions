class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_left = 0
        res_right = 0
        
        i = 0
        skip_forward: bool = False

        while i < len(s):
            left = right = i

            while right + 1 < len(s) and s[right + 1] == s[i]:
                skip_forward = True
                right += 1

            forward_i = right

            while left - 1 >= 0 and right + 1 < len(s) and s[left - 1] == s[right + 1]:
                left -= 1
                right += 1

            if right - left > res_right - res_left:
                res_right, res_left = right, left

            if skip_forward:
                skip_forward = False
                i = forward_i
            else:
                i += 1

        return s[res_left:res_right + 1]
