from collections import Counter
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.result = False

        word_counts = Counter(word)
        board_counts = Counter(char for row in board for char in row)
        
        for char, count in word_counts.items():
            if board_counts[char] < count:
                return False
            
        if board_counts[word[0]] > board_counts[word[-1]]:
            word = word[::-1]
        
        def search(row: int, col: int, word_idx: int, visited: set):
            if word_idx == len(word) - 1:
                 self.result = True
                 return
            
            visited.add((row, col))

            possible_pos = [
                 (row - 1, col), # up
                 (row + 1, col), # down
                 (row, col - 1), # left
                 (row, col + 1)  # right
            ]
            
            for pos in possible_pos:
                 if not(0 <= pos[0] < len(board) and    # check row valid
                        0 <= pos[1] < len(board[0]) and # check col valid
                        pos not in visited):            # check not visited
                      continue
                 
                 if board[pos[0]][pos[1]] != word[word_idx + 1]:
                     continue
                 
                 search(pos[0], pos[1], word_idx + 1, visited.copy())

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    search(row, col, word_idx=0, visited=set())
                if self.result:
                    return True
                
        return False
