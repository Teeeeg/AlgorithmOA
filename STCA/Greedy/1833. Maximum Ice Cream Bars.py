from typing import List


class Solution:

    def maxIceCream(self, costs: List[int], coins: int) -> int:
        sortedCost = sorted(costs, reverse=True)
        res = 0

        while sortedCost and coins >= sortedCost[-1]:
            coins -= sortedCost.pop()
            res += 1

        return res


costs = [1, 3, 2, 4, 1]
coins = 7
slt = Solution()
print(slt.maxIceCream(costs, coins))