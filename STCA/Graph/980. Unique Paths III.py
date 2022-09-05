from typing import List, Set


class GridType:
    OBSTACLE = -1
    EMPTY = 0
    START = 1
    END = 2


DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


class Solution:

    def isValid(self, grid: List[List[int]], row: int, col: int, visited: Set):
        return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and (row, col) not in visited

    def uniquePathsIIICore(self, grid: List[List[int]], visited: Set, row: int, col: int, count: int, end):
        if count == 0 and (row, col) == end:
            self.res += 1
            return

        for deltaX, deltaY in DIRS:
            newRow = row + deltaX
            newCol = col + deltaY

            if not self.isValid(grid, newRow, newCol, visited) or grid[newRow][newCol] == GridType.OBSTACLE:
                continue

            visited.add((newRow, newCol))
            self.uniquePathsIIICore(grid, visited, newRow, newCol, count - 1, end)
            visited.remove((newRow, newCol))

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        pathCount = 1
        start = None
        end = None
        visited = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == GridType.EMPTY:
                    pathCount += 1
                if grid[i][j] == GridType.START:
                    start = (i, j)
                if grid[i][j] == GridType.END:
                    end = (i, j)

        visited.add(start)
        self.res = 0
        self.uniquePathsIIICore(grid, visited, start[0], start[1], pathCount, end)

        return self.res


grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
slt = Solution()
print(slt.uniquePathsIII(grid))