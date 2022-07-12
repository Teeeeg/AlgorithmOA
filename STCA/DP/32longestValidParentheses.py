class Solution:

    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        res = 0

        # dp[i] 表示[0,i]字符串能组成有效括号的长度
        dp = [0] * n

        for i in range(1, n):
            # 若当前为( 则肯定为0
            if s[i] == '(':
                dp[i] = 0
            else:
                # 若当前为 )
                # 前一个为 (
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2
                # 前一个为 )
                # 则假设前一个 ) 已经匹配上， 需判断在匹配的 ( 之前是否有 (, 有则匹配上
                # s[i - 1 - dp[i - 1]] 表示匹配完成之前的字符
                elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    # 同时需要添加 dp[i - 2 - dp[i - 1]] 表示当前匹配之前的所有
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]

            if dp[i] > res:
                res = dp[i]

        return res


slt = Solution()
s = "()(())"
print(slt.longestValidParentheses(s))