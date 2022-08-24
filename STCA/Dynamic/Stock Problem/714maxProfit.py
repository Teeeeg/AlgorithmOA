from typing import List


class Solution:

    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        # opt[0][i] not holding
        # opt[1][i] holding
        opt = [[0] * n for _ in range(2)]
        opt[1][0] = -prices[0]

        for i in range(1, n):
            opt[0][i] = max(opt[0][i - 1], opt[1][i - 1] + prices[i] - fee)
            opt[1][i] = max(opt[1][i - 1], opt[0][i - 1] - prices[i])

        return opt[0][-1]


prices = [1, 3, 2, 8, 4, 9]
fee = 2
slt = Solution()
print(slt.maxProfit(prices, fee))
