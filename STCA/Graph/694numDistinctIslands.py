from typing import List


class Solution:
    # 记录相对位置后
    # 用set

    def numDistinctIslandsCore(self, grid: List[List[int]], cur, path):
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # 用于记录相对位置
        startX = cur[0]
        startY = cur[1]

        queue = [cur]
        while queue:
            cur = queue.pop(0)
            path.append((cur[0] - startX, cur[1] - startY))
            grid[cur[0]][cur[1]] = 0
            for dir in dirs:
                post = (cur[0] + dir[0], cur[1] + dir[1])
                if 0 <= post[0] < len(grid) and 0 <= post[1] < len(grid[0]) and grid[post[0]][post[1]]:
                    queue.append(post)

    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        islands = set()
        for i in range(m):
            for j in range(n):
                # 每个出发点记录
                if grid[i][j] == 1:
                    path = []
                    cur = (i, j)
                    self.numDistinctIslandsCore(grid, cur, path)
                    islands.add(tuple(path))

        return len(islands)


grid = [[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 1, 0, 1], [1, 1, 0, 1, 1]]
slt = Solution()
print(slt.numDistinctIslands(grid))
