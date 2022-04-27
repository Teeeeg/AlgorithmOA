from typing import List


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isWord = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.isWord

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True


class Solution:
    def __init__(self) -> None:
        self.root = None

    def buildTrie(self, words):
        trie = Trie()
        for word in words:
            trie.insert(word)
        self.root = trie.root

    def findPrefix(self, word):
        res = ''
        node = self.root
        for ch in word:
            if ch not in node.children or node.isWord:
                break
            res += ch
            node = node.children[ch]

        return res if node.isWord else ''

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        self.buildTrie(dictionary)
        sentence = sentence.split(' ')

        for i, word in enumerate(sentence):
            prefix = self.findPrefix(word)
            if prefix:
                sentence[i] = prefix

        return ' '.join(sentence)


solution = Solution()

dictionary = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"

print(solution.replaceWords(dictionary, sentence))
