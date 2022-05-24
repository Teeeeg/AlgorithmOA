class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        # 每次只可以走一步，每一步只可以从左边或者上边传递而来
        # 求最优解，用动态规划

        # dp[i][j]表示到[i,j] 位置的走法
        dp = [[0] * n for _ in range(m)]
        # 初始化
        # 左边一侧只可能从上面而来
        for i in range(m):
            dp[i][0] = 1
        # 上边一侧只可能从左边而来
        for i in range(n):
            dp[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                # 当前路径只可能从左边或者上边而来
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


slt = Solution()
print(slt.uniquePaths(3, 2))