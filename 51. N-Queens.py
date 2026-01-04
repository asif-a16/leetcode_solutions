class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        col = set()
        pos_diag = set() # row + col
        neg_diag = set() # row - col

        board = [["."] * n for _ in range(n)]
        
        def dfs(row):
            if row == n:
                result.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if c in col or (row + c) in pos_diag or (row - c) in neg_diag:
                    continue

                board[row][c] = "Q"
                col.add(c)
                pos_diag.add(row + c)
                neg_diag.add(row - c)

                dfs(row + 1)

                neg_diag.remove(row - c)
                pos_diag.remove(row + c)
                col.remove(c)
                board[row][c] = "."

        dfs(0)
        return result
