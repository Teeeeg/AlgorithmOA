from typing import List

DIRS = [(-1, 0), (1, 0), (0, 1), (0, -1)]


class DisjointSet:

    def __init__(self) -> None:
        self.root = {}
        self.sizeOfRoot = {}
        self.sizeOfSet = 0

    def add(self, x):
        if x in self.root:
            return False

        self.root[x] = x
        self.sizeOfSet += 1
        self.sizeOfRoot[x] = 1
        return True

    def find(self, x):
        if x == self.root.get(x, x):
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX
            self.sizeOfSet -= 1
            self.sizeOfRoot[rootX] += self.sizeOfRoot[rootY]

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)

    def getSizeOfSet(self):
        return self.sizeOfSet

    def getSizeOfRoot(self, x):
        return self.sizeOfRoot[x]

    def getAllSizes(self):
        return self.sizeOfRoot


class Solution:

    def isValid(self, grid: List[List[int]], row: int, col: int):
        return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        disjointSet = DisjointSet()

        for i in range(m):
            for j in range(n):
                if not grid[i][j] == 1:
                    continue
                disjointSet.add((i, j))
                for deltaX, deltaY in DIRS:
                    row = i + deltaX
                    col = j + deltaY
                    if not self.isValid(grid, row, col):
                        continue
                    disjointSet.add((row, col))
                    disjointSet.union((i, j), (row, col))

        sizes = disjointSet.getAllSizes()
        maxArea = 0
        if sizes:
            maxArea = max(sizes.values())

        return maxArea


grid = [[0, 0, 1], [1, 1, 1]]
slt = Solution()
print(slt.maxAreaOfIsland(grid))