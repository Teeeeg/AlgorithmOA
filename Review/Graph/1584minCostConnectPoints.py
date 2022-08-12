from typing import List


class DisjointSet:

    def __init__(self, size) -> None:
        self.root = [i for i in range(size)]

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX
            return True
        return False


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []

        for i in range(1, n):
            for j in range(i):
                z = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((i, j, z))

        edges.sort(key=lambda x: x[2])

        disjointSet = DisjointSet(n)
        res = 0
        for edge in edges:
            x = edge[0]
            y = edge[1]
            z = edge[2]
            if disjointSet.union(x, y):
                res += z

        return res
