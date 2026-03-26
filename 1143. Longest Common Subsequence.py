class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def recurse(text1_idx: int, text2_idx: int) -> int:
            if text1_idx >= len(text1) or text2_idx >= len(text2):
                return 0
            if text1[text1_idx] == text2[text2_idx]:
                return 1 + recurse(text1_idx + 1, text2_idx + 1)
            else:
                return max(recurse(text1_idx + 1, text2_idx), recurse(text1_idx, text2_idx + 1))
            
        return recurse(0, 0)
