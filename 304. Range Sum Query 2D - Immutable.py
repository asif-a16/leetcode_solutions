class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row_sum_matrix = [([0] * (len(matrix[0]) + 1)) for _ in range(len(matrix) + 1)]

        running_sum = 0
        for i in range(len(matrix)):
            for j, num in enumerate(matrix[i]):
                running_sum += num
                row_sum_matrix[i][j] = running_sum
            row_sum_matrix[i + 1][len(matrix[0])] = running_sum

        self.row_sum_matrix = row_sum_matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for row in range(row1, row2 + 1):
            total += self.row_sum_matrix[row][col2] - self.row_sum_matrix[row][col1 - 1]

        return total
    

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)