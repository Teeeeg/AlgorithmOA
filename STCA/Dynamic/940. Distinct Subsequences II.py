class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        MOD = 10 ** 9 + 7

        # the subsets with the last char of s[i]
        dp = [0] * n

        charSet = set()
        for i in range(n):
            if s[i] not in charSet:
                dp[i] = 1
            charSet.add(s[i])

        for i in range(n):
            for j in range(i - 1, -1, -1):
                dp[i] = (dp[i] + dp[j]) % MOD
                if s[i] == s[j]:
                    break

        return sum(dp) % MOD


s = "abc"
slt = Solution()
print(slt.distinctSubseqII(s))
