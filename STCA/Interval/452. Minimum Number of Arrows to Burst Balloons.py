from typing import List


class Solution:

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        sortedPoints = sorted(points, key=lambda x: (x[0], x[1]))

        res = 0
        pre = sortedPoints[0]

        for i in range(1, n):
            cur = sortedPoints[i]
            if cur[0] <= pre[1]:
                pre = [cur[0], min(pre[1], cur[1])]
            else:
                res += 1
                pre = cur

        return res + 1


points = [[7, 15], [6, 14], [8, 12], [3, 4], [4, 13], [6, 14], [9, 11], [6, 12], [4, 13]]
slt = Solution()
print(slt.findMinArrowShots(points))