# Definition for an Interval.
from heapq import heappop, heappush


class Interval:

    def __init__(self, start: int = None, end: int = None):  # type: ignore
        self.start = start
        self.end = end


class Solution:

    def employeeFreeTime(self, schedule: '[[Interval]]'):  # type: ignore
        minHeap = []
        for employee in schedule:
            for interval in employee:
                heappush(minHeap, (interval.start, -1))
                heappush(minHeap, (interval.end, 1))

        res = []
        matched = 0

        while minHeap:
            left, flag = heappop(minHeap)
            matched += flag

            if matched == 0 and minHeap:
                right = minHeap[0][0]
                interval = Interval(left, right)
                res.append(interval)

        return res
