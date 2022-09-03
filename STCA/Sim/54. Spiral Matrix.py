from typing import List


class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        leftBound = 0
        rightBound = n - 1
        upBound = 0
        bottomBound = m - 1
        res = []

        x = 0
        y = 0
        curDir = 0

        while len(res) < m * n:
            res.append(matrix[x][y])
            # finish upper layer, upBound get lower
            # etc..
            if curDir == 0 and y == rightBound:
                curDir += 1
                upBound += 1

            if curDir == 1 and x == bottomBound:
                curDir += 1
                rightBound -= 1

            if curDir == 2 and y == leftBound:
                curDir += 1
                bottomBound -= 1

            if curDir == 3 and x == upBound:
                curDir += 1
                leftBound += 1

            curDir = curDir % 4
            x += dirs[curDir][0]
            y += dirs[curDir][1]

        return res


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
slt = Solution()
print(slt.spiralOrder(matrix))