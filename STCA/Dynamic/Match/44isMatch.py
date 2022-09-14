class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        n1 = len(s)
        n2 = len(p)

        opt = [[False] * (n2 + 1) for _ in range(n1 + 1)]
        opt[0][0] = True

        for i in range(1, n2 + 1):
            opt[0][i] = opt[0][i - 1] and p[i - 1] == '*'

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    opt[i][j] = opt[i - 1][j - 1]
                elif p[j - 1] == '*':
                    opt[i][j] = opt[i - 1][j] or opt[i][j - 1]
                    # former source text from [0, i] to match *
                    # opt[i][j - 1] means use * match none
                    # backward to find if it can match, between them is *'s match
                    # for k in range(i + 1):
                    #     if opt[k][j - 1]:
                    #         opt[i][j] = True
                    #         break

        return opt[-1][-1]


s = "aab"
p = "c*a*b"
slt = Solution()
print(slt.isMatch(s, p))