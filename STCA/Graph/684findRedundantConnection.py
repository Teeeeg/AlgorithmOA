from typing import List


class DisjointSet:

    def __init__(self, size) -> None:
        self.size = size
        self.root = [i for i in range(self.size)]

    def find(self, x):
        if self.root[x] == x:
            return x

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
    # for each adding of the edges, if both vertex have been connected
    # this edge is a redundant one
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = DisjointSet(n + 1)

        for edge in edges:
            if uf.isConnected(edge[0], edge[1]):
                return edge
            uf.union(edge[0], edge[1])

        return []
