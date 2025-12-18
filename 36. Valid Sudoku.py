class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_t = list(zip(*board))
        
        def containsDuplicates(listt: List[str]) -> bool:
            for i in range(1, 10):
                if listt.count(str(i)) >= 2:
                    return True
            return False

        for row in board:
            if containsDuplicates(row):
                return False
            
        for col in board_t:
            if containsDuplicates(col):
                return False
            
        for col_idx in range(0, 9, 3):
            for row_idx in range(0, 9, 3):

                working = [
                    board[i][j] 
                    for i in range(row_idx, row_idx + 3) 
                    for j in range(col_idx, col_idx + 3)
                    ]
                
                if containsDuplicates(working):
                    return False
                
        return True
