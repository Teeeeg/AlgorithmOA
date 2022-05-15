class Solution:
    def fib(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 0:
            return 0

        dp = [0] * 2
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i % 2] = dp[(i - 1) % 2] + dp[i % 2]

        return dp[n % 2]


slt = Solution()
print(slt.fib(4))
