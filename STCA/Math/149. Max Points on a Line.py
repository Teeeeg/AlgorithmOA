from math import gcd
from typing import List


class Solution:

    def maxPoints(self, points: List[List[int]]) -> int:
        sortedPoints = sorted(points)
        n = len(sortedPoints)
        res = 0

        for i in range(n):
            slopeCount = {}
            x1, y1 = sortedPoints[i]

            for j in range(i + 1, n):
                x2, y2 = sortedPoints[j]
                dx = x2 - x1
                dy = y2 - y1

                curGCD = gcd(dx, dy)
                key = (dx // curGCD, dy // curGCD)
                slopeCount[key] = slopeCount.get(key, 0) + 1

                res = max(res, slopeCount[key])

        return res + 1


points = [[1, 1], [2, 2], [3, 3]]
slt = Solution()
print(slt.maxPoints(points))