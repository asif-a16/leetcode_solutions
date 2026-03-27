class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        row, col = 0, 0
        depth = 0

        mode = "right"

        while len(result) < len(matrix) * len(matrix[0]):
            match mode:
                case "right":
                    while col < len(matrix[0]) - depth:
                        result.append(matrix[row][col])
                        col += 1
                    col -= 1
                    row += 1
                    mode = "down"
                case "down":
                    while row < len(matrix) - depth:
                        result.append(matrix[row][col])
                        row += 1
                    row -= 1
                    col -= 1
                    mode = "left"
                case "left":
                    while col >= 0 + depth:
                        result.append(matrix[row][col])
                        col -= 1
                    col += 1
                    row -= 1
                    mode = "up"
                case "up":
                    while row >= 1 + depth:
                        result.append(matrix[row][col])
                        row -= 1
                    row += 1
                    col += 1
                    depth += 1
                    mode = "right"
            
        return result
