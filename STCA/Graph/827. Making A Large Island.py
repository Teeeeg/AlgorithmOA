from collections import deque
from typing import List

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


class Solution:

    def isLand(self, grid: List[List[int]], row: int, col: int):
        return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != 0

    def isValid(self, grid: List[List[int]], row: int, col: int):
        return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1

    def bfs(self, grid: List[List[int]], row: int, col: int, index: int):
        queue = deque([(row, col)])
        grid[row][col] = index
        area = 0

        while queue:
            row, col = queue.popleft()
            area += 1
            for deltaX, deltaY in DIRS:
                newRow = row + deltaX
                newCol = col + deltaY
                if not self.isValid(grid, newRow, newCol):
                    continue

                grid[newRow][newCol] = index
                queue.append((newRow, newCol))

        return index, area

    def getIsland(self, grid: List[List[int]]):
        island2Area = {}
        m = len(grid)
        n = len(grid[0])
        index = 2

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    curIndex, curArea = self.bfs(grid, i, j, index)
                    island2Area[curIndex] = curArea
                    index += 1

        return island2Area

    def largestIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        if not m or not n:
            return 0

        island2Area = self.getIsland(grid)
        maxArea = 0
        if island2Area:
            maxArea = max(island2Area.values())

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    continue
                area = 1
                visited = set()
                for deltaX, deltaY in DIRS:
                    row = deltaX + i
                    col = deltaY + j
                    if not self.isLand(grid, row, col):
                        continue

                    index = grid[row][col]
                    if index not in visited:
                        area += island2Area[index]
                    visited.add(index)

                maxArea = max(maxArea, area)

        return maxArea


grid = [[0, 0], [0, 0]]
slt = Solution()
print(slt.largestIsland(grid))