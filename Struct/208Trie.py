class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        root = self.root
        for ch in word:
            if ch not in root.children:
                root.children[ch] = TrieNode()
            root = root.children[ch]
        root.isWord = True

    def search(self, word: str) -> bool:
        root = self.root
        for ch in word:
            if ch not in root.children:
                return False
            root = root.children[ch]
        return root.isWord == True

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for ch in prefix:
            if ch in root.children:
                root = root.children[ch]
            else:
                return False

        return True
