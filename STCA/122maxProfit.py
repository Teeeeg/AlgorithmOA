from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # dp[i][0] 表示i天不持有股票的现金
        # dp[i][1] 表示i天持有股票的现金
        dp = [[0]*2 for _ in range(n)]
        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])

        return dp[-1][0]


class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        res = 0

        for i in range(1, n):
            profit = prices[i] - prices[i-1]
            if profit > 0:
                res += profit
        return res
