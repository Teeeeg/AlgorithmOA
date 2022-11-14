from collections import deque
from typing import List


class Solution:

    def removeStones(self, stones: List[List[int]]) -> int:
        graphX = {}
        graphY = {}

        for x, y in stones:
            graphX[x] = graphX.get(x, [])
            graphX[x].append(y)
            graphY[y] = graphY.get(y, [])
            graphY[y].append(x)

        visited = set()
        connectedCount = 0

        for x, y in stones:
            if (x, y) in visited:
                continue

            queue = deque()
            queue.append((x, y))

            while queue:
                curX, curY = queue.popleft()
                if (curX, curY) in visited:
                    continue

                visited.add((curX, curY))

                for nextY in graphX[curX]:
                    queue.append((curX, nextY))

                for nextX in graphY[curY]:
                    queue.append((nextX, curY))

            connectedCount += 1

        return len(stones) - connectedCount


class DisjointSet:

    def __init__(self) -> None:
        self.root = {}
        self.sizeOfSet = 0

    def add(self, x):
        if x in self.root:
            return

        self.root[x] = x
        self.sizeOfSet += 1

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])

        return self.root[x]

    def joint(self, x, y):
        root1 = self.find(x)
        root2 = self.find(y)

        if root1 != root2:
            self.root[root2] = root1
            self.sizeOfSet -= 1


class Solution1:

    def removeStones(self, stones: List[List[int]]) -> int:
        dSet = DisjointSet()
        pivot = 10**5

        for x, y in stones:
            dSet.add(x)
            dSet.add(y + pivot)

            dSet.joint(x, y + pivot)

        return len(stones) - dSet.sizeOfSet


stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
slt = Solution1()
print(slt.removeStones(stones))