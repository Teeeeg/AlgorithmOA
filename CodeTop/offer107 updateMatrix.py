import math
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        queue = []
        res = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))

        visited = set(queue)
        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        while queue:
            i, j = queue.pop(0)
            for dir in dirs:
                newI, newJ = i+dir[0], j+dir[1]
                if 0 <= newI < m and 0 <= newJ < n and (newI, newJ) not in visited:
                    res[newI][newJ] = res[i][j]+1
                    queue.append((newI, newJ))
                    visited.add((newI, newJ))
        return res

    def updateMatrix1(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        res = [[math.inf]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    res[i][j] = 0

        for i in range(m):
            for j in range(n):
                if 0 <= i-1 < m:
                    res[i][j] = min(res[i][j], res[i-1][j]+1)
                if 0 <= j-1 < n:
                    res[i][j] = min(res[i][j], res[i][j-1]+1)

        for i in range(m):
            for j in range(n-1, -1, -1):
                if 0 <= i-1 < m:
                    res[i][j] = min(res[i][j], res[i-1][j]+1)
                if 0 <= j+1 < n:
                    res[i][j] = min(res[i][j], res[i][j+1]+1)

        for i in range(m-1, -1, -1):
            for j in range(n):
                if 0 <= i+1 < m:
                    res[i][j] = min(res[i][j], res[i+1][j]+1)
                if 0 <= j-1 < n:
                    res[i][j] = min(res[i][j], res[i][j-1]+1)

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if 0 <= i+1 < m:
                    res[i][j] = min(res[i][j], res[i+1][j]+1)
                if 0 <= j+1 < n:
                    res[i][j] = min(res[i][j], res[i][j+1]+1)

        return res


mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
solution = Solution()
print(solution.updateMatrix1(mat))
