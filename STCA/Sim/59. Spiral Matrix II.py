from typing import List


class Solution:

    def generateMatrix(self, n: int) -> List[List[int]]:

        loopTime = n // 2
        matrix = [[0] * n for _ in range(n)]
        val = 1
        startX = 0
        startY = 0

        for offset in range(1, loopTime + 1):
            bound = n - offset
            for j in range(startY, bound):
                matrix[startX][j] = val
                val += 1

            for i in range(startX, bound):
                matrix[i][bound] = val
                val += 1

            for j in range(bound, startY, -1):
                matrix[bound][j] = val
                val += 1

            for i in range(bound, startX, -1):
                matrix[i][startY] = val
                val += 1

            startX += 1
            startY += 1

        if n % 2:
            matrix[n // 2][n // 2] = n**2

        return matrix
