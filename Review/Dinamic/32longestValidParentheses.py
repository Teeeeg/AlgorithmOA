class Solution:

    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0

        res = 0

        n = len(s)

        # dp[i] 表示 [0, i] 的括号数
        dp = [0] * n

        for i in range(1, n):
            if s[i] == '(':
                dp[i] = 0
            else:
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2
                elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]

            if dp[i] > res:
                res = dp[i]

        return res


s = "(()))())("
slt = Solution()
print(slt.longestValidParentheses(s))