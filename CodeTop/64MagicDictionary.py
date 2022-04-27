import re
from typing import List


class TreeNode:
    def __init__(self) -> None:
        self.children = {}
        self.isWord = False


class MagicDictionary:

    def __init__(self):
        self.root = TreeNode()

    def buildDict(self, dictionary: List[str]) -> None:
        node = self.root

        for word in dictionary:
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TreeNode()
                node = node.children[ch]
            node.isWord = True

    def search(self, searchWord: str) -> bool:
        return self.searchCore(self.root, searchWord, 0, 0)

    def searchCore(self, node, searchWord, index, count):
        if index > len(searchWord):
            return False
        if node.isWord and count <= 1 and index == len(searchWord):
            return True

        ch = searchWord[index]

        if ch in node.children:
            if self.searchCore(node.children[ch], searchWord, index+1, count):
                return True
        else:
            flag = False
            for ch in node.children.keys():
                flag = self.searchCore(
                    node.children[ch], searchWord, index+1, count+1)
                if flag:
                    return True

        return False


dct = MagicDictionary()
dct.buildDict(['hello', 'leetcode'])
# print(dct.search('hello'))
print(dct.search('hell'))
# print(dct.search('leetcoded'))
