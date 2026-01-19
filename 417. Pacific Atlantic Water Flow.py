class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        def dfs(row: int, col: int):
            possible_positions = [
                (row - 1, col), # up
                (row + 1, col), # down
                (row, col - 1), # left
                (row, col + 1)  # right
            ]

            for roww, coll in possible_positions:
                if roww < 0 or coll < 0:
                    pacific.add((row, col))
                    continue
                if roww >= len(heights) or coll >= len(heights[0]):
                    atlantic.add((row, col))
                    continue

                if (roww, coll) in atlantic:
                    atlantic.add((row, col))
                    continue
                if (roww, coll) in pacific:
                    pacific.add((row, col))
                    continue

                dfs(roww, coll)


        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if (row, col) in pacific or (row, col) in atlantic:
                    continue
                dfs(row, col)

        result = []
        for row, col in pacific:
            if (row, col) in atlantic:
                result.append([row, col])

        return result
