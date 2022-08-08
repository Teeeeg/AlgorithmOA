import math
from typing import List


class Solution:

    def __init__(self) -> None:
        self.pathCoin = []

    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0

        MAX = 2**31 - 1

        self.path = [-1] * (amount + 1)
        opt = [MAX] * (amount + 1)
        opt[0] = 0

        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if i - coins[j] >= 0:
                    if opt[i] > opt[i - coins[j]] + 1:
                        opt[i] = opt[i - coins[j]] + 1
                        self.path[i] = j

        self.getCoins(coins, amount)
        print(self.pathCoin)

        return opt[-1] if opt[-1] != MAX else -1

    def getCoins(self, coins, amount):
        if self.path[amount] == -1:
            return

        self.getCoins(coins, amount - coins[self.path[amount]])
        self.pathCoin.append(coins[self.path[amount]])


class Solution1:

    def coinChangeCore(self, amount) -> int:
        if amount == 0:
            return 0

        if amount < 0:
            return self.MAX

        if self.opt[amount] != -1:
            return self.opt[amount]

        self.opt[amount] = self.MAX
        for coin in self.coins:
            self.opt[amount] = min(self.opt[amount], self.coinChangeCore(amount - coin) + 1)

        return self.opt[amount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        self.MAX = 2**31 - 1

        self.coins = coins
        self.opt = [-1] * (amount + 1)

        res = self.coinChangeCore(amount)
        return res if res != self.MAX else -1


coins = [2, 5, 10, 1]
amount = 27

slt = Solution()
print(slt.coinChange(coins, amount))