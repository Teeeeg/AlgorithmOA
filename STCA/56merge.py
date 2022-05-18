from typing import List


class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        res = [intervals[0]]

        for i in range(1, n):
            lastInterval = res[-1]
            if lastInterval[1] >= intervals[i][0]:
                res[-1] = [
                    lastInterval[0],
                    max(lastInterval[0], intervals[i][1])
                ]
            else:
                res.append(intervals[i])

        return res


intervals = [[1, 3]]
slt = Solution()
print(slt.merge(intervals))