from typing import List


class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # opt[i][j] means the number of ways to [i,j]
        opt = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 0:
                    if i == 0 and j == 0:
                        opt[i][j] = 1
                    elif j == 0:
                        opt[i][0] = opt[i - 1][0]
                    elif i == 0:
                        opt[0][j] = opt[0][j - 1]
                    else:
                        opt[i][j] = opt[i - 1][j] + opt[i][j - 1]

        return opt[-1][-1]


class Solution1:

    def uniquePathsWithObstaclesCore(self, row, col):
        if row >= self.m or col >= self.n or self.obstacleGrid[row][col]:
            return 0

        if self.opt[row][col]:
            return self.opt[row][col]

        if row == self.m - 1 and col == self.n - 1:
            return 1

        self.opt[row][col] = self.uniquePathsWithObstaclesCore(row + 1, col) + self.uniquePathsWithObstaclesCore(row, col + 1)
        return self.opt[row][col]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.m = len(obstacleGrid)
        self.n = len(obstacleGrid[0])
        self.obstacleGrid = obstacleGrid
        self.opt = [[0] * self.n for _ in range(self.m)]
        return self.uniquePathsWithObstaclesCore(0, 0)


obstacleGrid = [[0, 0], [1, 1], [0, 0]]
slt = Solution1()
print(slt.uniquePathsWithObstacles(obstacleGrid))