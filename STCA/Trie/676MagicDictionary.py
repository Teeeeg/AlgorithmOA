from typing import List


class TrieNode:

    def __init__(self, value) -> None:
        self.value = value
        self.children = {}
        self.isWord = False


class MagicDictionary:

    def __init__(self):
        self.root = TrieNode('root')

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            node = self.root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode(ch)
                node = node.children[ch]
            node.isWord = True

    def searchCore(self, node: TrieNode, searchWord, index, modified):
        if index == len(searchWord):
            return modified and node.isWord

        ch = searchWord[index]

        if ch in node.children:
            if self.searchCore(node.children[ch], searchWord, index + 1, modified):
                return True

        if not modified:
            for key in node.children:
                if key != ch:
                    if self.searchCore(node.children[key], searchWord, index + 1, True):
                        return True

        return False

    def search(self, searchWord: str) -> bool:
        return self.searchCore(self.root, searchWord, 0, False)


strs = ["hello", "hallo", "leetcode"]
dct = MagicDictionary()
dct.buildDict(strs)
res = dct.search("hello")
print(res)