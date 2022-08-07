from typing import List


class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals or not intervals[0]:
            return []

        intervals.sort(key=lambda x: x[0])
        merged = []

        for interval in intervals:
            if merged and merged[-1][1] >= interval[0]:
                merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]
            else:
                merged.append(interval)

        return merged


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
slt = Solution()
print(slt.merge(intervals))