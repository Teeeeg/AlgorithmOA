class Solution:

    def minCut(self, s: str) -> int:
        n = len(s)
        matrix = [[False] * n for _ in range(n)]

        for i in range(n):
            for j in range(i, -1, -1):
                if s[i] != s[j]:
                    matrix[j][i] = False
                # 若为一个字符默认为回文
                # 否则从上一个[j+1, i-1] 上推导
                elif i - j <= 1 or matrix[j + 1][i - 1]:
                    matrix[j][i] = True

        # dp[i] 表示为[0, i] 最少切割次数
        # 显然dp[0]=0 因为只有一个的时候不需要切分
        dp = [i for i in range(n)]

        for i in range(1, n):
            if matrix[0][i]:
                dp[i] = 0
            for j in range(i):
                if matrix[j + 1][i]:
                    dp[i] = min(dp[j] + 1, dp[i])

        return dp[-1]


s = "aab"
slt = Solution()
print(slt.minCut(s))