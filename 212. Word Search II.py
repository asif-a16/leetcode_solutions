class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]

        cur.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()

        for word in words:
            trie.insert(word)

        result = []
        rows, cols = len(board), len(board[0])

        def search(row: int, col: int, cur_node: TrieNode):
            char = board[row][col]

            if char not in cur_node.children:
                return

            next_node = cur_node.children[char]

            if next_node.word != None:
                result.append(next_node.word)
                next_node.word = None

            board[row][col] = "#"

            possible_pos = [
                 (row - 1, col), # up
                 (row + 1, col), # down
                 (row, col - 1), # left
                 (row, col + 1)  # right
            ]

            for (i, j) in possible_pos:
                if not (
                    0 <= i < rows and   # check row valid
                    0 <= j < cols and   # check col valid
                    board[i][j] != "#"  # check not visited
                ):
                    continue

                search(i, j, next_node)

            board[row][col] = char

            # prune dead branches of trie
            if len(next_node.children) == 0 and next_node.word == None:
                del cur_node.children[char]

        for i in range(rows):
            for j, letter in enumerate(board[i]):
                if letter in trie.root.children:
                    search(i, j, trie.root)

        return result
