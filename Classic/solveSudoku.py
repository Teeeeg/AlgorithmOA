from typing import List


class Solution:

    def solveSudoku(self, board: List[List[str]]) -> None:
        self.solveSudokuCore(board)

    def solveSudokuCore(self, board):
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != '.':
                    continue
                for num in range(1, 10):
                    if self.isValid(board, row, col, num):
                        board[row][col] = str(num)
                        if self.solveSudokuCore(board):
                            return True
                        board[row][col] = '.'
                return False
        return True

    def isValid(self, board, row, col, num):
        n = len(board)
        # 行
        for i in range(n):
            if board[i][col] == str(num):
                return False
        # 列
        for i in range(n):
            if board[row][i] == str(num):
                return False
        # 九宫格
        # 第几个九宫格，乘以其宽度
        rowStart = (row // 3) * 3
        colStart = (col // 3) * 3

        for i in range(rowStart, rowStart + 3):
            for j in range(colStart, colStart + 3):
                if board[i][j] == str(num):
                    return False

        return True