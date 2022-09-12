from typing import List


class Solution:

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sortedIntervals = sorted(intervals, key=lambda x: x[1])
        end = sortedIntervals[0][1]
        nonOverLapped = 1

        for interval in sortedIntervals:
            if interval[0] >= end:
                nonOverLapped += 1
                end = max(interval[1], end)

        return len(intervals) - nonOverLapped


intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
slt = Solution()
print(slt.eraseOverlapIntervals(intervals))
