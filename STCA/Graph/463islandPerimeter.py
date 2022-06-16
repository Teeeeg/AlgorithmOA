from typing import List


class Solution:

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    source = [i, j]
                    perimeter = self.getPerimeter(visited, grid, source)
                    res += perimeter

        return res

    def getPerimeter(self, visited, grid, source):
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m = len(grid)
        n = len(grid[0])
        queue = [source]
        visited[source[0]][source[1]] = True
        perimeter = 0

        while queue:
            # 当前节点
            cur = queue.pop(0)
            for dir in dirs:
                # next为cur的四个方向
                next = [dir[0] + cur[0], dir[1] + cur[1]]
                # 若其四边在水边和在边界，周长+1
                if next[0] < 0 or next[0] >= m or next[1] < 0 or next[1] >= n or grid[next[0]][next[1]] == 0:
                    perimeter += 1
                # 否则是土地，则添加入队列
                elif grid[next[0]][next[1]] == 1 and not visited[next[0]][next[1]]:
                    queue.append(next)
                    visited[next[0]][next[1]] = True

        return perimeter

    def islandPerimeter1(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        res = 0

        for i in range(m):
            for j in range(n):
                cur = [i, j]
                if grid[i][j] == 1:
                    for dir in dirs:
                        post = [cur[0] + dir[0], cur[1] + dir[1]]
                        if post[0] < 0 or post[1] < 0 or post[0] >= m or post[1] >= n or grid[post[0]][
                                post[1]] == 0 or grid[post[0]][post[1]] == 0:
                            res += 1

        return res


grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
slt = Solution()
print(slt.islandPerimeter1(grid))