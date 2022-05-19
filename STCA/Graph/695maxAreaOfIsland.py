from typing import List


class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    source = [i, j]
                    area = self.getArea(grid, visited, source)
                    res = max(res, area)

        return res

    def getArea(self, grid, visited, source):
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m = len(grid)
        n = len(grid[0])

        queue = [source]
        visited[source[0]][source[1]] = True
        area = 0

        while queue:
            cur = queue.pop(0)
            area += 1

            for dir in dirs:
                next = [dir[0] + cur[0], dir[1] + cur[1]]
                if 0 <= next[0] < m and 0 <= next[1] < n and grid[next[0]][
                        next[1]] == 1 and not visited[next[0]][next[1]]:
                    queue.append(next)
                    visited[next[0]][next[1]] = True

        return area


grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
slt = Solution()
print(slt.maxAreaOfIsland(grid))