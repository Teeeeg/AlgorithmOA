from typing import List


class Solution:

    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i] 表示凑i的方法数
        dp = [0] * (amount + 1)
        dp[0] = 1

        # 组合问题 顺序无关
        # 所以先遍历物品，再遍历容量
        for coin in coins:
            for i in range(1, amount + 1):
                if i - coin >= 0:
                    dp[i] += dp[i - coin]

        return dp[-1]


amount = 5
coins = [1, 2, 5]
slt = Solution()
print(slt.change(amount, coins))