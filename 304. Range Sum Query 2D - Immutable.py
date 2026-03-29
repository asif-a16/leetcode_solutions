class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        sum_matrix = [[0] * (n + 1) for _ in range(m + 1)]

        for row in range(m):
            running_sum = 0
            for col, num in enumerate(matrix[row]):
                running_sum += num
                running_sum_above = sum_matrix[row - 1][col]
                sum_matrix[row][col] = running_sum + running_sum_above

        self.sum_matrix = sum_matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        above = self.sum_matrix[row1 - 1][col2]
        bottom_right = self.sum_matrix[row2][col2]
        left = self.sum_matrix[row2][col1 - 1]
        top_left = self.sum_matrix[row1 - 1][col1 - 1]

        return bottom_right - left - above + top_left
    
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
