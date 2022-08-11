from typing import List


class TrieNode:

    def __init__(self, ch) -> None:
        self.children = {}
        self.ch = ch
        self.isWord = ''


class Trie:

    def __init__(self):
        self.root = TrieNode('root')

    def insert(self, word: str) -> None:
        root = self.root
        for ch in word:
            if ch not in root.children:
                root.children[ch] = TrieNode(ch)
            root = root.children[ch]
        root.isWord = word


class Solution:
    # Trie dfs with graph dfs

    def findWordsCore(self, row, col, node: TrieNode):
        if node.isWord:
            self.res.append(node.isWord)
            node.isWord = ''

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        root = node

        for dir in dirs:
            nr = row + dir[0]
            nc = col + dir[1]

            if 0 <= nr < self.m and 0 <= nc < self.n and not self.visited[nr][nc]:
                if self.board[nr][nc] not in node.children:
                    continue

                node = node.children[self.board[nr][nc]]
                self.visited[nr][nc] = 1
                self.findWordsCore(nr, nc, node)
                self.visited[nr][nc] = 0
                node = root

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.m = len(board)
        self.n = len(board[0])

        self.board = board
        self.words = words
        self.visited = [[0] * self.n for _ in range(self.m)]
        self.res = []

        trie = Trie()
        for word in words:
            trie.insert(word)

        root = trie.root
        for row in range(self.m):
            for col in range(self.n):
                if self.board[row][col] in root.children:
                    self.visited[row][col] = 1
                    self.findWordsCore(row, col, root.children[self.board[row][col]])
                    self.visited[row][col] = 0

        return self.res


board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
words = ["oath", "pea", "eat", "rain", "oathi", "oathk", "oathf", "oate", "oathii", "oathfi", "oathfii"]
slt = Solution()
print(slt.findWords(board, words))
