from typing import List


class Solution:
    # 从边缘出发，标记从边缘出发的O为S
    # 第二次遍历，若标记为S，表明此节点未被包围，则重新标为O
    # 若标记为O，表明该节点被包围，标记为X

    def dfs(self, board: List[List[str]], row: int, col: int):
        m = len(board)
        n = len(board[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # 若当前节点不是O则return
        if board[row][col] != 'O':
            return
        # 标记为S
        board[row][col] = 'S'

        for dir in dirs:
            nextRow = row + dir[0]
            nextCol = col + dir[1]
            # 递归，深度优先
            if 0 <= nextRow < m and 0 <= nextCol < n and board[nextRow][nextCol] == 'O':
                self.dfs(board, nextRow, nextCol)

    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])

        for i in range(n):
            self.dfs(board, 0, i)
            self.dfs(board, m - 1, i)

        for i in range(m):
            self.dfs(board, i, 0)
            self.dfs(board, i, n - 1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'S':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'


board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
slt = Solution()
slt.solve(board)
print(board)