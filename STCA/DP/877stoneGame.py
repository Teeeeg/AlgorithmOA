from typing import List


class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)

        # dp[i][j] 表示[i, j] 范围内先手获得的最大相对分数
        # 显然对角线为0
        # 且这个区间必须包括两个元素
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1):
            for j in range(i + 1, n):
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])

        return dp[0][n - 1] > 0


piles = [5, 3, 4, 5]
slt = Solution()
print(slt.stoneGame(piles))