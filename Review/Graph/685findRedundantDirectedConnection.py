from typing import List


class UnionFind:

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
    # [u, v] u -> v
    # a tree add one edge it will have two vertex with two indegree
    # if it has no two indegree, it go normal unionfind
    def isTree(self, edges: List[List[int]], removable: List[int]):
        # use unionfind to judge it is a tree or not
        n = len(edges)
        uf = UnionFind(n + 1)
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
        # count indegrees
        for edge in edges:
            inDegrees[edge[1]] += 1

        # get twodegree vertex
        twoDegreeVertex = 0
        for i in range(n + 1):
            if inDegrees[i] == 2:
                twoDegreeVertex = i

        removable = []
        # if it has two indegrees
        if twoDegreeVertex != 0:
            # get edges
            for edge in edges:
                if twoDegreeVertex == edge[1]:
                    removable.append(edge)
            # return the last one, so judge the last first
            if self.isTree(edges, removable[1]):
                return removable[1]
            else:
                return removable[0]

        uf = UnionFind(n + 1)
        # if it do not have two indegrees
        for edge in edges:
            if uf.isConnected(edge[0], edge[1]):
                return edge
            uf.union(edge[0], edge[1])

        return []


edges = [[2, 1], [3, 1], [4, 2], [1, 4]]
slt = Solution()
print(slt.findRedundantDirectedConnection(edges))
