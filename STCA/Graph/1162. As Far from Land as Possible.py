from collections import deque
from typing import List


class GridType:
    OCEAN = 0
    LAND = 1


class Solution:

    def isValid(self, grid: List[List[int]], row: int, col: int, dist):
        return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and (row, col) not in dist

    def maxDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        dist = {}
        maxDist = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] != GridType.LAND:
                    continue
                queue.append((i, j))
                dist[(i, j)] = 0

        if not queue or len(queue) == m * n:
            return -1

        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while queue:
            row, col = queue.popleft()
            for deltaX, deltaY in dirs:
                newRow = row + deltaX
                newCol = col + deltaY

                if not self.isValid(grid, newRow, newCol, dist):
                    continue

                dist[(newRow, newCol)] = dist[(row, col)] + 1
                maxDist = max(dist[(newRow, newCol)], maxDist)
                queue.append((newRow, newCol))

        return maxDist


grid = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
slt = Solution()
print(slt.maxDistance(grid))