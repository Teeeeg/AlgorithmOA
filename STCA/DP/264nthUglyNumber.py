class Solution:

    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1

        # 分别表示由2，3，5作为下个质因子丑数的下标
        index2 = 0
        index3 = 0
        index5 = 0

        for i in range(1, n):
            dp[i] = min(dp[index2] * 2, dp[index3] * 3, dp[index5] * 5)
            # 更新下标
            if dp[i] == dp[index2] * 2:
                index2 += 1
            if dp[i] == dp[index3] * 3:
                index3 += 1
            if dp[i] == dp[index5] * 5:
                index5 += 1

        return dp[-1]


n = 10
slt = Solution()
print(slt.nthUglyNumber(n))