class Solution:

    def numSquares(self, n: int) -> int:
        MAX = 10**9 + 7

        dp = [MAX] * (n + 1)
        dp[0] = 0

        # cache squares
        squares = [x**2 for x in range(1, n + 1) if x**2 <= n]

        for num in range(1, n + 1):
            for sqr in squares:
                if num - sqr < 0:
                    break
                dp[num] = min(dp[num], dp[num - sqr] + 1)

        return dp[-1]


n = 8935
slt = Solution()
print(slt.numSquares(n))