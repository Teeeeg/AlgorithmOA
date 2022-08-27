from typing import List


class Solution:

    def isValid(self, matrix: List[List[int]], row, col, newRow, newCol):
        m = len(matrix)
        n = len(matrix[0])

        return 0 <= newRow < m and 0 <= newCol < n and matrix[row][col] < matrix[newRow][newCol]

    def longestIncreasingPathCore(self, matrix: List[List[int]], row, col, memo):
        if memo[row][col] != -1:
            return memo[row][col]

        DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        memo[row][col] = 0
        for deltaRow, deltaCol in DIRS:
            newRow = row + deltaRow
            newCol = col + deltaCol

            if not self.isValid(matrix, row, col, newRow, newCol):
                continue

            memo[row][col] = max(memo[row][col], self.longestIncreasingPathCore(matrix, newRow, newCol, memo) + 1)

        return memo[row][col]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        res = 0
        memo = [[-1] * n for _ in range(m)]

        for row in range(m):
            for col in range(n):
                res = max(res, self.longestIncreasingPathCore(matrix, row, col, memo) + 1)

        return res


matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
slt = Solution()
print(slt.longestIncreasingPath(matrix))