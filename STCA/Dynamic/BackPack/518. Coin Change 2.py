from typing import List


class Solution:

    def change(self, amount: int, coins: List[int]) -> int:
        opt = [0] * (amount + 1)
        opt[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                opt[i] += opt[i - coin]

        return opt[-1]


amount = 5
coins = [1, 2, 5]
slt = Solution()
print(slt.change(amount, coins))
