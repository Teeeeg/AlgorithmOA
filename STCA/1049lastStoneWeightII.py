from typing import List


class Solution:

    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        total = sum(stones)
        target = total // 2

        # dp[i] 表示i容量 能凑到最大石头的重量
        dp = [0] * (target + 1)

        for i in range(n):
            for j in range(target, stones[i] - 1, -1):
                # for j in reversed(range(stones[i], target + 1)):
                dp[j] = max(dp[j - stones[i]] + stones[i], dp[j])

        return total - 2 * dp[-1]


stones = [2, 7, 4, 1, 8, 1]
slt = Solution()
print(slt.lastStoneWeightII(stones))
