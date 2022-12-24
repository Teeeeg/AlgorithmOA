class Solution:

    def numTilings(self, n):
        if n < 3:
            return n
        MOD = 10**9 + 7

        # dp[0] denotes the number of ways to tile an 2 * i board
        # dp[1] denotes the number of ways to tile an 2 * i board and one more square left

        dp = [[0] * (n + 1) for _ in range(2)]
        dp[0][1] = 1
        dp[0][2] = 2
        dp[1][1] = 0
        dp[1][2] = 1

        for i in range(3, n + 1):
            # use vertically + horizontally + 2 * one square left (up and below)
            dp[0][i] = dp[0][i - 1] + dp[0][i - 2] + 2 * dp[1][i - 1]
            # use a trio + a horizontal brick
            dp[1][i] = dp[0][i - 2] + dp[1][i - 1]

        return dp[0][-1] % MOD


n = 4
slt = Solution()
print(slt.numTilings(n))