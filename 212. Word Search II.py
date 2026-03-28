class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_terminal = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]

        cur.is_terminal = True
    
    def isPrefix(self, prefix: str, root: TrieNode = None):
        cur = self.root

        if root != None:
            cur = root

        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]

        return cur
    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()

        for word in words:
            trie.insert(word)

        result = set()

        def search(row: int, col: int, word_builder: List[str], visited: set, root: TrieNode = None):
            word_builder.append(board[row][col])

            if root and root.is_terminal:
                result.add("".join(word_builder))

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
                
                next_node = trie.isPrefix(board[pos[0]][pos[1]], root)
                
                if not next_node:
                    continue
                
                search(pos[0], pos[1], word_builder[:], visited.copy(), next_node)

        for i in range(len(board)):
            for j, letter in enumerate(board[i]):
                next_node = trie.isPrefix(letter)
                if next_node:
                    search(i, j, [], set(), next_node)

        return list(result)
