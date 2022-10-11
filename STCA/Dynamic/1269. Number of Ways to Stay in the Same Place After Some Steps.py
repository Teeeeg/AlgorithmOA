class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:
        # dp[i][j] the num of ways when step i stay at j
        n = min(steps // 2 + 1, arrLen)
        dp = [[0] * n for _ in range(steps + 1)]
        dp[0][0] = 1
        MOD = 10**9 + 7

        for i in range(1, steps + 1):
            for j in range(n):
                dp[i][j] += dp[i - 1][j]
                dp[i][j] %= MOD
                if j > 0:
                    dp[i][j] += dp[i - 1][j - 1]
                    dp[i][j] %= MOD

                if j < n - 1:
                    dp[i][j] += dp[i - 1][j + 1]
                    dp[i][j] %= MOD

        return dp[-1][0]


steps = 3
arrLen = 2
slt = Solution()
print(slt.numWays(steps, arrLen))