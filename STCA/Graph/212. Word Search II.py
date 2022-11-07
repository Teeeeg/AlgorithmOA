from typing import List


class TrieNode:

    def __init__(self):
        self.children = {}
        self.word = ''


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root

        for char in word:
            if char not in root.children:
                root.children[char] = TrieNode()
            root = root.children[char]

        root.word = word


class Solution:

    def buildTrie(self, words: List[str]):
        trie = Trie()

        for word in words:
            trie.insert(word)

        return trie

    def isValid(self, board: List[List[str]], node, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] in node.children

    def findWordsCore(self, board: List[List[str]], x, y, node, visited, res):
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        if node.word:
            res.append(node.word)
            node.word = ''

        for deltaX, deltaY in dirs:
            newX = x + deltaX
            newY = y + deltaY

            if not self.isValid(board, node, newX, newY) or visited[newX][newY]:
                continue

            visited[newX][newY] = 1
            self.findWordsCore(board, newX, newY, node.children[board[newX][newY]], visited, res)
            visited[newX][newY] = 0

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        trie = self.buildTrie(words)
        root = trie.root
        visited = [[0] * n for _ in range(m)]
        res = []

        for i in range(m):
            for j in range(n):
                if board[i][j] not in root.children:
                    continue

                visited[i][j] = 1
                self.findWordsCore(board, i, j, root.children[board[i][j]], visited, res)
                visited[i][j] = 0

        return res
