class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str):
        n1 = len(text1)
        n2 = len(text2)

        # dp[i][j] 表示1中0-i-1，2中0-j-1最长公共子序列的长度
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        # 用于输出
        res = []

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    # 最长的一定是从此传递过来的
                    res.append(text1[i - 1])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # # 输出该子串
        # res = []
        # for i in range(n1, 0, -1):
        #     for j in range(n2, 0, -1):
        #         if dp[i][j] > dp[i - 1][j] and dp[i][j] > dp[i][j - 1]:
        #             res.append(text1[i - 1])

        # return list(reversed(res))

        return res


text1 = "abc"
text2 = "def"
slt = Solution()
print(slt.longestCommonSubsequence(text1, text2))