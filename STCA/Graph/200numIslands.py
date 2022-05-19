from typing import List


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    # 每次找到一个新入口，岛屿数量加一
                    res += 1
                    # 利用bfs把访问过的岛屿标记
                    self.bfs(visited, grid, [i, j])

        return res

    # 广度优先
    def bfs(self, visited, grid, source):
        m = len(grid)
        n = len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # 每次入队的时候标记访问
        queue = [source]
        visited[source[0]][source[1]] = True

        while queue:
            # 当前节点
            cur = queue.pop(0)
            for dir in dirs:
                next = [dir[0] + cur[0], dir[1] + cur[1]]
                if 0 <= next[0] < m and 0 <= next[1] < n and grid[next[0]][
                        next[1]] == '1' and not visited[next[0]][next[1]]:
                    queue.append(next)
                    visited[next[0]][next[1]] = True


grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]

slt = Solution()
print(slt.numIslands(grid))