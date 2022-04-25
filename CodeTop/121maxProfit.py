import math
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        res = 0

        for i in range(n):
            for j in range(i+1, n):
                res = max(res, prices[j]-prices[i])

        return res

    def maxProfit1(self, prices: List[int]) -> int:
        minPrice = math.inf
        res = 0

        for price in prices:
            res = max(price-minPrice, res)
            minPrice = min(price, minPrice)

        return res


solution = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(solution.maxProfit1(prices))
