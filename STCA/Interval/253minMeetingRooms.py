from heapq import heappop, heappush
from typing import List


class Solution:

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        minHeap = []

        # 每次和最先结束的会议进行比较
        for interval in intervals:
            if minHeap and interval[0] >= minHeap[0][0]:
                heappop(minHeap)
            heappush(minHeap, [interval[1], interval[0]])

        return len(minHeap)


intervals = [[0, 30], [5, 10], [15, 20]]
slt = Solution()
print(slt.minMeetingRooms(intervals))