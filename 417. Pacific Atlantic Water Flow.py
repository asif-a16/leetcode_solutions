from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visit, prev_height):
            if ((r, c) in visit or
                r < 0 or c < 0 or r == m or c == n or
                heights[r][c] < prev_height):
                return
            
            visit.add((r, c))
            possible_positions = [
                (r + 1, c), # down
                (r, c + 1), # right
                (r - 1, c), # up
                (r, c - 1)  # down
            ]

            for row, col in possible_positions:
                dfs(row, col, visit, heights[r][c])

        for c in range(n):
            dfs(0, c, pacific, heights[0][c])
            dfs(m - 1, c, atlantic, heights[m - 1][c])

        for r in range(m):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, n - 1, atlantic, heights[r][n - 1])

        return list(atlantic & pacific)
