class Solution:

    def __init__(self) -> None:
        self.LCS = ''

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        text1 = ' ' + text1
        text2 = ' ' + text2
        self.text = text1

        # opt[i, j] means length of i and length of j's LCS
        opt = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        self.path = [[-1] * (n2 + 1) for _ in range(n1 + 1)]

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if text1[i] == text2[j]:
                    opt[i][j] = opt[i - 1][j - 1] + 1
                    self.path[i][j] = 0
                else:
                    if opt[i - 1][j] >= opt[i][j - 1]:
                        opt[i][j] = opt[i - 1][j]
                        self.path[i][j] = 1

                    else:
                        opt[i][j] = opt[i][j - 1]
                        self.path[i][j] = 2

        self.getPath(n1, n2)
        print(self.LCS)

        return opt[-1][-1]

    def getPath(self, i, j):
        if i <= 0 and j <= 0:
            return

        if self.path[i][j] == 0:
            self.getPath(i - 1, j - 1)
            self.LCS += self.text[i]
        elif self.path[i][j] == 1:
            self.getPath(i - 1, j)
        else:
            self.getPath(i, j - 1)


text1 = "abc"
text2 = "abc"
slt = Solution()
print(slt.longestCommonSubsequence(text1, text2))