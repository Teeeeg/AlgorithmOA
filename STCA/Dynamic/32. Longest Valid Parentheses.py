class Solution:

    def longestValidParentheses(self, s: str) -> int:
        n = len(s)

        opt = [0] * n
        res = 0

        for i in range(1, n):
            if s[i] == '(':
                opt[i] = 0
            else:
                if i - 1 - opt[i - 1] >= 0 and s[i - 1 - opt[i - 1]] == '(':
                    opt[i] = opt[i - 1] + 2
                    if i - 2 - opt[i - 1] >= 0:
                        opt[i] += opt[i - 2 - opt[i - 1]]

            if res < opt[i]:
                res = opt[i]

        return res


s = '()'
slt = Solution()
print(slt.longestValidParentheses(s))