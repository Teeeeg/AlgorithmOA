from typing import List


class Solution:

    def numIslandsCore(self, row, col):
        self.grid[row][col] = '0'

        for dir in self.dirs:
            nr = row + dir[0]
            nc = col + dir[1]
            if 0 <= nr < self.m and 0 <= nc < self.n and self.grid[nr][nc] == '1':
                self.numIslandsCore(nr, nc)

    def numIslands(self, grid: List[List[str]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        self.grid = grid
        self.dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        res = 0

        for row in range(self.m):
            for col in range(self.n):
                if self.grid[row][col] == '1':
                    self.numIslandsCore(row, col)
                    res += 1

        return res


grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]

slt = Solution()
print(slt.numIslands(grid))