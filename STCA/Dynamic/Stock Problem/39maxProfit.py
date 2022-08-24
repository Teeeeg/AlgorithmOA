from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # opt[0][i] not holding
        # opt[1][i] not holding + cooldown
        # opt[2][i] holding
        opt = [[0] * n for _ in range(3)]
        opt[2][0] = -prices[0]

        for i in range(1, n):
            opt[0][i] = max(opt[0][i - 1], opt[2][i - 1] + prices[i])
            opt[1][i] = opt[0][i - 1]
            opt[2][i] = max(opt[2][i - 1], opt[1][i - 1] - prices[i])

        return opt[0][-1]


prices = [1, 2, 3, 0, 2]
slt = Solution()
print(slt.maxProfit(prices))
