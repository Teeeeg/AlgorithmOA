class Solution:

    def translateNum(self, num: int) -> int:
        source = str(num)
        n = len(source)

        # dp[i] 表示 前i个字符 的翻译方法
        dp = [0] * (n + 1)
        # 没有显然只有一个
        dp[0] = 1

        for i in range(1, n + 1):
            # 显然可以直接从前面传递
            dp[i] += dp[i - 1]
            num = int(source[i - 2]) * 10 + int(source[i - 1])
            # 可不可以形成两位
            if i > 1 and 10 <= num < 26:
                dp[i] += dp[i - 2]

        return dp[-1]


num = 18580
slt = Solution()
print(slt.translateNum(num))