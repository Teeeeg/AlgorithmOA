from typing import List


class UnionFind:

    def __init__(self, size) -> None:
        self.root = [i for i in range(size + 1)]

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n)

        for edge in edges:
            if uf.isConnected(edge[0], edge[1]):
                return edge
            uf.union(edge[0], edge[1])

        return []


edges = [[1, 2], [1, 3], [2, 3]]
slt = Solution()
print(slt.findRedundantConnection(edges))