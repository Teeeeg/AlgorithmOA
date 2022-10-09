from typing import List


class Solution:

    def isValid(self, board: List[List[str]], word, x, y, index, visited):
        return 0 <= x < len(board) \
            and 0 <= y < len(board[0]) \
            and board[x][y] == word[index] \
            and (x, y) not in visited

    def existCore(self, board: List[List[str]], word: str, x, y, index, visited):
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        if index == len(word):
            return True

        for deltaX, deltaY in dirs:
            nextX = x + deltaX
            nextY = y + deltaY

            if not self.isValid(board, word, nextX, nextY, index, visited):
                continue

            visited.add((nextX, nextY))
            if self.existCore(board, word, nextX, nextY, index + 1, visited):
                return True
            visited.remove((nextX, nextY))

        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        n1 = len(word)

        if n1 == 0:
            return True

        if m * n < n1:
            return False

        visited = set()

        for i in range(m):
            for j in range(n):
                if not board[i][j] == word[0]:
                    continue

                visited.add((i, j))
                if self.existCore(board, word, i, j, 1, visited):
                    return True
                visited.remove((i, j))

        return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "SEE"
slt = Solution()
print(slt.exist(board, word))