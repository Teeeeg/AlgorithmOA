from typing import Any, Counter, List


class TrieNode:

    def __init__(self) -> None:
        self.children = {}
        self.isWord = False


class Solution:

    def __init__(self) -> None:
        self.res = []

    def build(self, words: List[str]):
        counter = Counter(words)
        self.bucket = [Any] * len(words)

        for word, freq in counter.items():
            if self.bucket[freq] is None:
                self.bucket[freq] = TrieNode()
            node = self.bucket[freq]
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.isWord = True

    def getWord(self, node: TrieNode, word: str):
        if node.isWord and self.k > 0:
            self.res.append(word)
            self.k -= 1
        for i in range(26):
            ch = chr(ord('a') + i)
            if ch in node.children:
                self.getWord(node.children[ch], word + ch)

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        self.build(words)
        self.k = k

        for i in range(len(words) - 1, -1, -1):
            if self.bucket[i]:
                self.getWord(self.bucket[i], '')

        return self.res


words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 3

slt = Solution()
print(slt.topKFrequent(words, k))
