from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        loopTime = n//2
        matrix = [[0]*n for _ in range(n)]
        val = 1
        startX = 0
        startY = 0

        for offset in range(1, loopTime+1):

            for j in range(startY, n-offset):
                matrix[startX][j] = val
                val += 1

            for i in range(startX, n-offset):
                matrix[i][n-offset] = val
                val += 1

            for j in reversed(range(startY+1, n-offset+1)):
                matrix[n-offset][j] = val
                val += 1

            for i in reversed(range(startX+1, n-offset+1)):
                matrix[i][startY] = val
                val += 1

            startX += 1
            startY += 1

        if n % 2:
            matrix[n//2][n//2] = n**2

        return matrix


solution = Solution()
matrix = solution.generateMatrix(4)
for row in matrix:
    print(row)
