from typing import List


class Solution:

    def isValid(self, row, col):
        n = len(self.board[0])

        # column
        for i in range(row, -1, -1):
            if self.board[i][col] == 'Q':
                return False

        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if self.board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        i = row - 1
        j = col + 1
        while i >= 0 and j < n:
            if self.board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True

    def getResult(self):
        res = []
        for i in range(self.n):
            res.append(''.join(self.board[i]))
        return res

    def solveNQueensCore(self, row):
        if row == self.n:
            self.res.append(self.getResult())
            return

        for col in range(self.n):
            if self.isValid(row, col):
                self.board[row][col] = 'Q'
                self.solveNQueensCore(row + 1)
                self.board[row][col] = '.'

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.res = []
        self.board = [['.'] * n for _ in range(n)]
        self.solveNQueensCore(0)
        return self.res


slt = Solution()
print(slt.solveNQueens(1))