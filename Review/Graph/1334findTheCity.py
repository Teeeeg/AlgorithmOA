from typing import List


class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        MAX = (2 << 31) - 1
        dist = [[MAX] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0

        for edge in edges:
            x = edge[0]
            y = edge[1]
            z = edge[2]
            dist[x][y] = z
            dist[y][x] = z

        # Floyd
        # dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        # k is label, i, j are vertice
        # through [i, j], label not bigger than k's shortest path
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        res = 0
        resCount = n

        for i in range(n):
            count = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    count += 1
            if count <= resCount:
                res = i
                resCount = count

        return res


n = 4
edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
distanceThreshold = 4
slt = Solution()
print(slt.findTheCity(n, edges, distanceThreshold))
