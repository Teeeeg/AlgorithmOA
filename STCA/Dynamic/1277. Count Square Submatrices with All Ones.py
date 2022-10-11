from typing import List


class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        # dp[i][j] is the count of the square with the end of (i, j)
        dp = [[0] * n for _ in range(m)]
        # longest of the left
        leftBound = [[0] * n for _ in range(m)]
        # longest of the top
        topBound = [[0] * n for _ in range(m)]
        res = 0

        for i in range(m):
            dp[i][0] = leftBound[i][0] = matrix[i][0]
            res += dp[i][0]

        for j in range(1, n):
            dp[0][j] = topBound[0][j] = matrix[0][j]
            res += dp[0][j]

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    continue
                leftBound[i][j] = leftBound[i][j - 1] + 1
                topBound[i][j] = topBound[i - 1][j] + 1
                dp[i][j] = min(leftBound[i][j - 1], topBound[i - 1][j], dp[i - 1][j - 1]) + 1

                res += dp[i][j]

        return res


matrix = [[1, 0, 1], [1, 1, 0], [1, 1, 0]]
slt = Solution()
print(slt.countSquares(matrix))