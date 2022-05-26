import math
from typing import List


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        # dp[i] 表示凑成i价值所需要的最少硬币数
        # 因为求最小值，初始化最大值
        dp = [math.inf] * (amount + 1)
        # 初始化
        dp[0] = 0

        for i in range(n):
            for j in range(coins[i], amount + 1):
                dp[j] = min(dp[j - coins[i]], dp[j])

        return int(dp[-1]) if dp[-1] != math.inf else -1


coins = [2147483647]
amount = 2
slt = Solution()
print(slt.coinChange(coins, amount))