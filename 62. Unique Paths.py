class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        
        cache = {}

        for col in range(n):
            cache[(m - 1, col)] = 1
        for row in range(m):
            cache[(row, n - 1)] = 1

        def get_paths(r, c):
            if (r + 1, c) not in cache:
                get_paths(r + 1, c)
            if (r, c + 1) not in cache:
                get_paths(r, c + 1)
            
            cache[(r, c)] = cache[(r, c + 1)] + cache[(r + 1, c)]

        get_paths(0, 0)
        return cache[(0, 0)]
