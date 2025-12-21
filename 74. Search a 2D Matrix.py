class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m * n - 1

        while left <= right:
            pivot = left + int((right - left) / 2)
            q, r = divmod(pivot, n)
            if target == matrix[q][r]:
                return True
            elif target < matrix[q][r]:
                right = pivot - 1
            else:
                left = pivot + 1

        return False
