from typing import List


class Solution:

    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7
        # dp[i][j][k] is the count of last i poject at people of j and profit of k
        dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(len(group) + 1)]
        dp[0][0][0] = 1
        res = 0

        for i in range(1, len(group) + 1):
            for j in range(n + 1):
                for k in range(minProfit + 1):
                    dp[i][j][k] = (dp[i][j][k] + dp[i - 1][j][k]) % MOD

                    if j - group[i - 1] < 0:
                        continue

                    preProfit = max(0, k - profit[i - 1])
                    dp[i][j][k] = (dp[i][j][k] + dp[i - 1][j - group[i - 1]][preProfit]) % MOD

        for i in range(n + 1):
            res += dp[-1][i][minProfit]

        return res % MOD


n = 10
minProfit = 5
group = [2, 3, 5]
profit = [6, 7, 8]

slt = Solution()
print(slt.profitableSchemes(n, minProfit, group, profit))