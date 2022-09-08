from typing import List


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = 10**9 + 7
        # opt[i] is the minimum coin in acmount of i
        opt = [MAX] * (amount + 1)
        opt[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                opt[i] = min(opt[i], opt[i - coin] + 1)

        return opt[-1] if opt[-1] != MAX else -1