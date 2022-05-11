from typing import List


class Solution:
    def maxProfit(self, prices: List[int]):
        n = len(prices)
        # dp[i][0] 表示不持有股票的现金
        # dp[i][1] 表示持有股票的现金
        dp = [[0]*2 for _ in range(n)]
        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1], -prices[i])

        return dp[-1][0]


prices = [7, 1, 5, 3, 6, 4]
# prices1 = [7, 6, 4, 3, 1]
solution = Solution()
print(solution.maxProfit(prices))
