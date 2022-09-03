from heapq import heappop, heappush
from typing import List


class Solution:
    # effect
    # prefix sum

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        boundaries = []
        for interval in intervals:
            boundaries.append((interval[0], 1))
            boundaries.append((interval[1], -1))

        boundaries.sort()
        matched = 0

        res = 0

        for boundary in boundaries:
            matched += boundary[1]
            res = max(res, matched)

        return res


class Solution1:
    # effect
    # prefix sum

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        minHeap = []
        for interval in intervals:
            # -1 is start's flag
            # [1, 2(1)] [2(2), 3] is one meeting room
            # 2(1) should be in front
            heappush(minHeap, (interval[0], 1))
            heappush(minHeap, (interval[1], -1))

        res = 0
        matched = 0

        while minHeap:
            matched += heappop(minHeap)[1]
            res = max(res, matched)

        return res
