class TrieNode:
    # 定义节点
    def __init__(self) -> None:
        self.children = {}
        self.isWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # 获取root点
        node = self.root
        for ch in word:
            # 依次向下遍历，若无则创建
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        # 最后要标记为isWord
        node.isWord = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            # 若不存在则返回False
            if ch not in node.children:
                return False
            node = node.children[ch]
        # 返回isWord
        return node.isWord

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        # 不需要返回isWord
        return True
