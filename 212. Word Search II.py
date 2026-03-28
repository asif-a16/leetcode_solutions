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

        def search(row: int, col: int, word_builder: List[str], visited: set, cur_node: TrieNode = None):
            word_builder.append(board[row][col])

            if cur_node and cur_node.is_terminal:
                result.add("".join(word_builder))

            visited.add((row, col))
            
            possible_pos = [
                 (row - 1, col), # up
                 (row + 1, col), # down
                 (row, col - 1), # left
                 (row, col + 1)  # right
            ]

            for (i, j) in possible_pos:
                if not(0 <= i < len(board) and         # check row valid
                    0 <= j < len(board[0]) and         # check col valid
                    (i, j) not in visited and          # check not visited
                    board[i][j] in cur_node.children): # check in children
                    continue

                next_node = cur_node.children[board[i][j]]
                search(i, j, word_builder[:], visited.copy(), next_node)

        for i in range(len(board)):
            for j, letter in enumerate(board[i]):
                next_node = trie.isPrefix(letter)
                if next_node:
                    search(i, j, [], set(), next_node)

        return list(result)
