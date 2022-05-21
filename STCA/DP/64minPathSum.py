from typing import List


class Solution:

    def minPathSum(self, grid: List[List[int]]) -> int:
        # 当前节点只能从左边或者上传递过来
        # 只关心左和上，不关注过程
        # 因此选用动态规划
        m = len(grid)
        n = len(grid[0])

        # dp[i][j] 表示对于（i，j）这个点来说从（0，0）出发的最小路径和
        dp = [[0] * n for _ in range(m)]
        # 初始化
        dp[0][0] = grid[0][0]
        # 针对每一行
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        # 针对每一列
        for i in range(1, n):
            dp[0][i] = dp[0][i - 1] + grid[0][i]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[-1][-1]


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
slt = Solution()
print(slt.minPathSum(grid))