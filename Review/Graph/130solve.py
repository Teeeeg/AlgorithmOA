from typing import List


class Solution:

    def solveCore(self, row, col, flag, target):
        self.board[row][col] = target

        for dir in self.dirs:
            nr = row + dir[0]
            nc = col + dir[1]
            if 0 <= nr < self.m and 0 <= nc < self.n and self.board[nr][nc] == flag:
                self.solveCore(nr, nc, flag, target)

    def solve(self, board: List[List[str]]) -> None:
        # use df/bfs to tag
        if not board and not board[0]:
            return

        self.board = board
        self.m = len(self.board)
        self.n = len(self.board[0])
        self.dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        for row in range(self.m):
            if self.board[row][0] == 'O':
                self.solveCore(row, 0, 'O', 'S')

        for col in range(self.n):
            if self.board[0][col] == 'O':
                self.solveCore(0, col, 'O', 'S')

        for col in range(self.n):
            if self.board[self.m - 1][col] == 'O':
                self.solveCore(self.m - 1, col, 'O', 'S')

        for row in range(self.m):
            if self.board[row][self.n - 1] == 'O':
                self.solveCore(row, self.n - 1, 'O', 'S')

        # iterate through to change
        for row in range(self.m):
            for col in range(self.n):
                if self.board[row][col] == 'S':
                    self.board[row][col] = 'O'
                elif self.board[row][col] == 'O':
                    self.board[row][col] = 'X'


board = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]

slt = Solution()
slt.solve(board)
print(board)