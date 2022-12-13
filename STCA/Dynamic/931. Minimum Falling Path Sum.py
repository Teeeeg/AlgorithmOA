from typing import List

MAX = 10**9 + 7


class Solution:

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        dp = [[MAX] * n for _ in range(m + 1)]

        for i in range(n):
            dp[0][i] = 0

        for i in range(1, m + 1):
            for j in range(n):
                if j - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
                if j + 1 < n:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j + 1])

                dp[i][j] = min(dp[i][j], dp[i - 1][j])
                dp[i][j] += matrix[i - 1][j]

        return min(dp[-1])


matrix = [[-19, 57], [-40, -5]]
slt = Solution()
print(slt.minFallingPathSum(matrix))