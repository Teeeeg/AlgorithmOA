from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = [[0] * n for _ in range(4)]

        dp[1][0] = -prices[0]

        for i in range(1, n):
            dp[0][i] = max(dp[0][i - 1], dp[2][i - 1])
            dp[1][i] = max(dp[0][i - 1] - prices[i], dp[1][i - 1])
            dp[2][i] = dp[1][i - 1] + prices[i]
            dp[3][i] = dp[2][i - 1]

        return max(dp[0][-1], dp[1][-1], dp[2][-1])


prices = [1, 2, 3, 0, 2]
slt = Solution()
print(slt.maxProfit(prices))