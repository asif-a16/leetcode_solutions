class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        longer, shorter = text1, text2

        if len(text2) > len(text1):
            longer, shorter = text2, text1

        if longer == shorter:
            return len(longer)
        
        lengths = [0] * len(longer)
        
        short_pointer = 0

        for i, letter in enumerate(longer):
            if letter == shorter[0]:
                lengths[i] = 1
                short_pointer = 1
            elif letter == shorter[short_pointer]:
                lengths[i] = lengths[i-1] + 1
                short_pointer += 1
                if short_pointer == len(shorter):
                    return len(shorter)
                
        return max(lengths)
