class Solution:
    # 考虑以一个结尾 和 以两个结尾的情况
    def numDecodings(self, s: str) -> int:
        n = len(s)

        # dp[i] 表示有i个字符的解码数
        dp = [0] * (n + 1)
        # 初始化没有数的时候
        # 为了保证dp[1] 和 dp[2] 推导的准确性
        dp[0] = 1

        for i in range(1, n + 1):
            # 此时这个字符不为零，显然可以从之前推导
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            # 在上面的基础上
            # 判断这个数是否可以和前一个数组合
            # 可以和前一个组合
            if i > 1 and s[i - 2] != 0 and 10 <= int(s[i - 2] + s[i - 1]) <= 26:
                dp[i] += dp[i - 2]

        return dp[-1]


s = "2611055971756562"
slt = Solution()
print(slt.numDecodings(s))