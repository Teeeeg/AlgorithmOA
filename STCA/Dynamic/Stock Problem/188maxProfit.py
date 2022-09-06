from typing import List


class Solution:

    def maxProfit(self, k: int, prices: List[int]) -> int:
        # opt[i][even] to sell
        # opt[i][odd] to buy
        # opt[0][0] init
        n = len(prices)
        if not prices:
            return 0

        opt = [[0] * n for _ in range((2 * k + 1))]
        # init every init buying
        for j in range(1, 2 * k + 1, 2):
            opt[j][0] = -prices[0]

        for i in range(1, n):
            for j in range(1, 2 * k + 1, 2):
                # odd
                opt[j][i] = max(opt[j][i - 1], opt[j - 1][i - 1] - prices[i])
                # even
                opt[j + 1][i] = max(opt[j + 1][i - 1], opt[j][i - 1] + prices[i])

        return opt[-1][-1]


class Solution1:

    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)

        # 0: buy
        # 1: sold
        opt = [[0] * n for _ in range(2)]
        opt[0][0] = -prices[0]

        for i in range(1, n):
            for j in range(2 * k):
                if not j % 2:
                    opt[0][i] = max(opt[0][i - 1], opt[1][i - 1] - prices[i])
                else:
                    opt[1][i] = max(opt[1][i - 1], opt[0][i - 1] + prices[i])

        return opt[1][-1]


k = 2
prices = [3, 3, 5, 0, 0, 3, 1, 4]
slt = Solution()
print(slt.maxProfit(k, prices))