from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        res = 0

        for i in range(1, n):
            profit = prices[i] - prices[i - 1]
            if profit > 0:
                res += profit

        return res