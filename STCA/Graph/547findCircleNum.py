from typing import List


class DisjointSet:

    def __init__(self, size) -> None:
        self.root = [i for i in range(size)]
        # 要用一个count
        self.count = size

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX
            self.count -= 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = DisjointSet(n)

        for x in range(n):
            for y in range(x + 1, n):
                if isConnected[x][y] == 1:
                    uf.union(x, y)

        return uf.count


isConnected = [[1, 1, 1, 0, 1, 1, 1, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 1, 0, 0], [1, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0, 1, 0], [1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 1, 0, 1, 0], [0, 1, 0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 1, 0, 0, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]]
slt = Solution()
print(slt.findCircleNum(isConnected))