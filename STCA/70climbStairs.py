class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        # dp[i] 表示到第i阶的爬法
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[-1]


solution = Solution()
print(solution.climbStairs(2))
