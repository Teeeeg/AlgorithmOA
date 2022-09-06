from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # opt[0][i] means to sold
        # opt[1][i] means to buy
        opt = [[0] * n for _ in range(2)]
        opt[1][0] = -prices[0]

        for i in range(1, n):
            opt[0][i] = max(opt[0][i - 1], opt[1][i - 1] + prices[i])
            opt[1][i] = max(opt[1][i - 1], opt[0][i - 1] - prices[i])

        return opt[0][-1]


prices = [3, 3, 5, 0, 0, 3, 1, 4]
slt = Solution()
print(slt.maxProfit(prices))