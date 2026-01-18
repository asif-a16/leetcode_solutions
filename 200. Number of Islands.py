class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        m, n = len(grid), len(grid[0])
        islands = 0

        def searchIsland(row: int, col: int):
            possible_positions = [
                (row - 1, col), # up
                (row + 1, col), # down
                (row, col - 1), # left
                (row, col + 1)  # right
            ]

            for row, col in possible_positions:
                if (row < 0 or row >= m or
                    col < 0 or col >= n or
                    grid[row][col] == "0" or
                    (row, col) in visited):
                    continue

                visited.add((row, col))
                searchIsland(row, col)

        for row in range(m):
            for col in range(n):
                if (row, col) not in visited and int(grid[row][col]):
                    visited.add((row, col))
                    searchIsland(row, col)
                    islands += 1

        return islands
