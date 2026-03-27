class Node:
    def __init__(self):
        self.children = {}
        self.is_terminal = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = Node()
            cur = cur.children[char]

        cur.is_terminal = True
        

    def search(self, word: str, root: Node = None) -> bool:
        cur = self.root

        if root != None:
            cur = root

        for i, char in enumerate(word):
            if char == ".":
                return any([self.search(word[i + 1:], cur.children[child]) for child in cur.children.keys()])
            elif char not in cur.children:
                return False
            else:
                cur = cur.children[char]
        
        return cur.is_terminal


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)