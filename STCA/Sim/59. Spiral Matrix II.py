from typing import List


class Solution:

    def generateMatrix(self, n: int) -> List[List[int]]:
        count = 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        leftBound = 0
        rightBound = n - 1
        upperBound = 0
        bottomBound = n - 1
        matrix = [[0] * n for _ in range(n)]

        x = 0
        y = 0
        curDir = 0
        val = 1

        while count < n * n:
            matrix[x][y] = val

            if curDir == 0 and y == rightBound:
                curDir += 1
                upperBound += 1

            if curDir == 1 and x == bottomBound:
                curDir += 1
                rightBound -= 1

            if curDir == 2 and y == leftBound:
                curDir += 1
                bottomBound -= 1

            if curDir == 3 and x == upperBound:
                curDir += 1
                leftBound += 1

            curDir %= 4
            x += dirs[curDir][0]
            y += dirs[curDir][1]
            val += 1
            count += 1

        return matrix


n = 3
slt = Solution()
print(slt.generateMatrix(n))