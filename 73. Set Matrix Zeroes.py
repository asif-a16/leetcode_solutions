class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroed_rows = [0] * len(matrix)
        zeroed_cols = [0] * len(matrix[0])

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    zeroed_rows[row] = 1
                    zeroed_cols[col] = 1

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if zeroed_rows[row] or zeroed_cols[col]:
                    matrix[row][col] = 0
