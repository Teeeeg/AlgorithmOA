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
            self.root[rootX] = rootY

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:

    def isTree(self, edges: List[List[int]], removable: List[int]):
        uf = UnionFind(len(edges))
        for edge in edges:
            if edge == removable:
                continue
            if uf.isConnected(edge[0], edge[1]):
                return False
            uf.union(edge[0], edge[1])
        return True

    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        inDegrees = [0] * (n + 1)
        twoDegrees = 0

        for edge in edges:
            inDegrees[edge[1]] += 1

        for i in range(n, -1, -1):
            inDegree = inDegrees[i]
            if inDegree == 2:
                twoDegrees = i

        removables = []
        if twoDegrees != 0:
            for edge in edges:
                if twoDegrees == edge[1]:
                    removables.append(edge)

        if removables:
            if self.isTree(edges, removables[1]):
                return removables[1]
            else:
                return removables[0]

        uf = UnionFind(len(edges))

        for edge in edges:
            if uf.isConnected(edge[0], edge[1]):
                return edge
            uf.union(edge[0], edge[1])

        return []


edges = [[1, 5], [3, 2], [2, 4], [4, 5], [5, 3]]
slt = Solution()
print(slt.findRedundantDirectedConnection(edges))