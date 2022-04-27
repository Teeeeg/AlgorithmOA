from typing import List


# 回溯
class Solution:
    def __init__(self) -> None:
        self.res = 0

    def maxProfit(self, prices: List[int]) -> int:
        self.recursiveCore(prices, 0, 0, 0)
        return self.res

    def recursiveCore(self, prices, status, index, profit):
        if index == len(prices):
            self.res = max(self.res, profit)
            return

        self.recursiveCore(prices, status, index+1, profit)

        if status == 1:
            self.recursiveCore(prices, 0, index+1, profit+prices[index])
        else:
            self.recursiveCore(prices, 1, index+1, profit-prices[index])


# 动态规划


    def maxProfit1(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][1] = - prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][0]-prices[i], dp[i-1][1])

        return dp[n-1][0]


# 贪心算法


    def maxProfit2(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            profit += max(prices[i]-prices[i-1], 0)
        return profit


prices = [7, 1, 5, 3, 6, 4]
solution = Solution()
print(solution.maxProfit2(prices))
