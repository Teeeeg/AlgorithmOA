class Solution:

    def numTrees(self, n: int) -> int:
        if n == 1:
            return 1

        # dp[i] 表示 [1-i] 互不相同的个数
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        # dp[i] 可拆分成许多许多不同的组合
        for i in range(2, n + 1):
            for j in range(i):
                # dp[i] 由各种不同的组合组成
                dp[i] += dp[j] * dp[i - j - 1]

        return dp[-1]


slt = Solution()
print(slt.numTrees(4))