class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        row_below = [0] * (len(text2) + 1)
    
        for i in range(len(text1) - 1, -1, -1):
            current_row = [0] * (len(text2) + 1)

            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    current_row[j] = 1 + row_below[j + 1]
                else:
                    current_row[j] = max(row_below[j], current_row[j + 1])

            row_below = current_row

        return row_below[0]
