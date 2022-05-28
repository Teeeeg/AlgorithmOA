from typing import List


class TrieNode:

    def __init__(self) -> None:
        self.children = {}
        self.isWord = False


class Solution:

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for ch in word.split('/'):
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isWord = True

    # 不同于startWith
    # 判断当前节点在字典树当中是否有前缀
    def hasPrefix(self, word: str):
        node = self.root
        # 切分，因为有的文件为多字符
        for ch in word.split('/'):
            if ch not in node.children:
                return False
            node = node.children[ch]
            # True代表前缀出现
            if node.isWord:
                return True
        return True

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # 先排序，可以边更新字典树边记录结果
        folder.sort()
        res = set()
        for word in folder:
            # 当前在字典树中无前缀
            if not self.hasPrefix(word):
                res.add(word)
                self.insert(word)

        return list(res)


folder = ["/a/b/c", "/a/b/ca", "/a/b/d"]
slt = Solution()
print(slt.removeSubfolders(folder))
