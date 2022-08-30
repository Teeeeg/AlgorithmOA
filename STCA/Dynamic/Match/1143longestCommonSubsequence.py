class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)

        # opt[i][j] is the LCS of prevous length i, j text
        opt = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                context = 1 if text1[i - 1] == text2[j - 1] else 0
                opt[i][j] = max(opt[i][j - 1], opt[i - 1][j], opt[i - 1][j - 1] + context)

        return opt[-1][-1]
