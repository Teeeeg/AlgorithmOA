class Solution:

    def numDecodings(self, s: str) -> int:
        n = len(s)

        # dp[i] 表示 i 个字符的解码数目
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            if i > 1 and '10' <= s[i - 2] + s[i - 1] <= '26':
                dp[i] += dp[i - 2]

        return dp[-1]


s = "226"
slt = Solution()
print(slt.numDecodings(s))