from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        
        def bfs_from_ocean(start_cells):
            queue = deque(start_cells)
            visited = set(start_cells)
            
            while queue:
                r, c = queue.popleft()
                for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < m and 0 <= nc < n and 
                        (nr, nc) not in visited and 
                        heights[nr][nc] >= heights[r][c]):
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return visited
        
        pacific_start = [(0, c) for c in range(n)] + [(r, 0) for r in range(1, m)]
        pacific_reachable = bfs_from_ocean(pacific_start)
         
        atlantic_start = [(m-1, c) for c in range(n)] + [(r, n-1) for r in range(m-1)]
        atlantic_reachable = bfs_from_ocean(atlantic_start)
        
        return list(pacific_reachable & atlantic_reachable)
