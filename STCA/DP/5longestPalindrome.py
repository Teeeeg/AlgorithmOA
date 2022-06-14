class Solution:

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxLen = 0
        res = ''

        # dp[j][i] 表示[j, i] 是不是回文串
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            for j in range(i, -1, -1):
                if s[i] != s[j]:
                    dp[j][i] = False
                elif i - j <= 1 or dp[j + 1][i - 1]:
                    dp[j][i] = True
                    if i - j + 1 > maxLen:
                        res = s[j:i + 1]
                        maxLen = i - j + 1

        return res


s = "aaaa"
slt = Solution()
print(slt.longestPalindrome(s))