from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # 0 init
        # 1 to buy 1
        # 2 to sell 1
        # 3 to buy 2
        # 4 to sell 2

        opt = [[0] * n for _ in range(5)]
        # first buying
        opt[1][0] = -prices[0]
        # second buying, buy first and sold and then buy
        opt[3][0] = -prices[0]

        for i in range(1, n):
            opt[1][i] = max(opt[1][i - 1], opt[0][i - 1] - prices[i])
            opt[2][i] = max(opt[2][i - 1], opt[1][i - 1] + prices[i])
            opt[3][i] = max(opt[3][i - 1], opt[2][i - 1] - prices[i])
            opt[4][i] = max(opt[4][i - 1], opt[3][i - 1] + prices[i])

        return max(opt[2][-1], opt[4][-1])


prices = [3, 3, 5, 0, 0, 3, 1, 4]
slt = Solution()
print(slt.maxProfit(prices))