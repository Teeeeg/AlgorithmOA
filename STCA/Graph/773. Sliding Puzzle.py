from collections import deque
from typing import List


class Solution:

    def isValid(self, x, y):
        return 0 <= x < 2 and 0 <= y < 3

    def getNextStates(self, state, curX, curY):
        neighbors = []
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        for deltaX, deltaY in dirs:
            nextX = curX + deltaX
            nextY = curY + deltaY

            if not self.isValid(nextX, nextY):
                continue

            nextState = [row[:] for row in state]
            nextState[curX][curY], nextState[nextX][nextY] = nextState[nextX][nextY], nextState[curX][curY]
            neighbors.append((nextState, (nextX, nextY)))

        return neighbors

    def getBoardString(self, board: List[List[int]]):
        boardString = ''
        for row in board:
            boardString += ''.join(map(str, row))

        return boardString

    def getZeroIndex(self, board: List[List[int]]):
        for i in range(2):
            for j in range(3):
                if board[i][j] == 0:
                    return (i, j)
        return (0, 0)

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        x, y = self.getZeroIndex(board)
        queue = deque()
        queue.append((board[:], (x, y)))
        dist = {self.getBoardString(board): 0}

        while queue:
            curState, (curX, curY) = queue.popleft()
            curSateStr = self.getBoardString(curState)

            if curSateStr == '123450':
                return dist[curSateStr]

            for nextState, nextIndex in self.getNextStates(curState, curX, curY):
                nextStateStr = self.getBoardString(nextState)
                if nextStateStr in dist:
                    continue
                dist[nextStateStr] = dist[curSateStr] + 1
                queue.append((nextState, nextIndex))

        return -1


board = [[4, 1, 2], [5, 0, 3]]
slt = Solution()
print(slt.slidingPuzzle(board))