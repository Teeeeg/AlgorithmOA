from typing import List


class DisjointSet:

    def __init__(self, size) -> None:
        self.root = [i for i in range(size)]
        self.count = size

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def uinon(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            self.root[rootY] = rootX
            self.count -= 1

    def getCount(self):
        return self.count


class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        disjointSet = DisjointSet(n)

        for i in range(n):
            for j in range(i):
                if isConnected[i][j]:
                    disjointSet.uinon(i, j)

        return disjointSet.getCount()


isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
slt = Solution()
print(slt.findCircleNum(isConnected))
