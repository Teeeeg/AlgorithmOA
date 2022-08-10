from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # 0 buy 1
        # 1 sell 1
        # 2 buy 2
        # 3 sell 2

        opt = [[0] * n for _ in range(4)]
        # first buying
        opt[0][0] = -prices[0]
        # second buying, buy first and sold and then buy
        opt[2][0] = -prices[0]

        for i in range(1, n):
            opt[0][i] = max(opt[0][i - 1], -prices[i])
            opt[1][i] = max(opt[1][i - 1], opt[0][i - 1] + prices[i])
            opt[2][i] = max(opt[2][i - 1], opt[1][i - 1] - prices[i])
            opt[3][i] = max(opt[3][i - 1], opt[2][i - 1] + prices[i])

        return max(opt[1][-1], opt[3][-1])

