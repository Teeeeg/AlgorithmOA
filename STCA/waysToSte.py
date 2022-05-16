class Solution:

    def waysToStep(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [0] * (3)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i % 3] = (dp[(i - 1) % 3] + dp[(i - 2) % 3] +
                         dp[(i - 3) % 3]) % 1000000007

        return dp[n % 3]


slt = Solution()
print(slt.waysToStep(3))