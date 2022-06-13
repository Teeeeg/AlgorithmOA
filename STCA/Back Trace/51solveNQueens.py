from typing import List


class Solution:

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        res = []
        self.solveNQueensCore(n, board, res, 0)
        return res

    def solveNQueensCore(self, n, board, res, row):
        if n == row:
            tmpRes = []
            for tmp in board:
                tmpRes.append(''.join(tmp))
            res.append(tmpRes)
            return

        for col in range(n):
            if self.isValid(board, row, col):
                board[row][col] = 'Q'
                self.solveNQueensCore(n, board, res, row + 1)
                board[row][col] = '.'

    def isValid(self, board, row, col):
        # 列
        for i in range(len(board)):
            if board[i][col] == 'Q':
                return False

        # 左上
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # 右上
        i = row - 1
        j = col + 1
        while i >= 0 and j < len(board):
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True