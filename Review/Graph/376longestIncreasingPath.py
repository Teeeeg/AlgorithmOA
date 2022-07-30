from collections import defaultdict
from typing import List


class Solution:

    def isValid(self, matrix, row, col, newRow, newCol):
        return 0 <= newRow < self.m and 0 <= newCol < self.n and matrix[newRow][newCol] > matrix[row][col]

    def longestIncreasingPathCore(self, matrix: List[List[int]], row, col):
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        if self.memo[row][col]:
            return self.memo[row][col]

        self.memo[row][col] += 1

        for dir in dirs:
            newRow = row + dir[0]
            newCol = col + dir[1]
            if self.isValid(matrix, row, col, newRow, newCol):
                self.memo[row][col] = max(self.memo[row][col],
                                          self.longestIncreasingPathCore(matrix, newRow, newCol) + 1)

        return self.memo[row][col]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.memo = [[0] * self.n for _ in range(self.m)]

        res = 0

        for i in range(self.m):
            for j in range(self.n):
                res = max(res, self.longestIncreasingPathCore(matrix, i, j))

        return res


class Solution1:

    def isValid(self, matrix, row, col, newRow, newCol):
        return 0 <= newRow < self.m and 0 <= newCol < self.n and matrix[newRow][newCol] < matrix[row][col]

    def getGraph(self, matrix: List[List[int]], inDegrees, graph, source):
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                inDegree = 0
                dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dir in dirs:
                    newRow = row + dir[0]
                    newCol = col + dir[1]
                    if self.isValid(matrix, row, col, newRow, newCol):
                        graph[(newRow, newCol)].append((row, col))
                        inDegree += 1
                inDegrees[row][col] = inDegree
                if inDegrees[row][col] == 0:
                    source.append((row, col))

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.m = len(matrix)
        self.n = len(matrix[0])
        inDegrees = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        graph = defaultdict(list)
        source = []
        step = 0

        self.getGraph(matrix, inDegrees, graph, source)

        while source:
            n = len(source)
            for _ in range(n):
                row, col = source.pop(0)
                for newRow, newCol in graph[(row, col)]:
                    inDegrees[newRow][newCol] -= 1
                    if inDegrees[newRow][newCol] == 0:
                        source.append((newRow, newCol))
            step += 1

        return step


matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
slt = Solution1()
print(slt.longestIncreasingPath(matrix))