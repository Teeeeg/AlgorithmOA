class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0

        n1 = len(text1)
        n2 = len(text2)

        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        pathMark = [[0] * (n2) for _ in range(n1)]

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    pathMark[i - 1][j - 1] = 1
                else:
                    if dp[i][j - 1] > dp[i - 1][j]:
                        dp[i][j] = dp[i][j - 1]
                        pathMark[i - 1][j - 1] = 2
                    else:
                        dp[i][j] = dp[i - 1][j]
                        pathMark[i - 1][j - 1] = 3
        path = []
        self.getPath(pathMark, n1 - 1, n2 - 1, path, text1)
        print(''.join(path))

        return dp[-1][-1]

    def getPath(self, pathMark, i, j, path, text):
        if i < 0 or j < 0:
            return

        if pathMark[i][j] == 1:
            self.getPath(pathMark, i - 1, j - 1, path, text)
            path.append(text[i])
        elif pathMark[i][j] == 2:
            self.getPath(pathMark, i, j - 1, path, text)
        else:
            self.getPath(pathMark, i - 1, j, path, text)


text1 = "abc"
text2 = "def"
slt = Solution()
print(slt.longestCommonSubsequence(text1, text2))