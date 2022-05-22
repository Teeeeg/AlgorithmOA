from heapq import heappop, heappush
from typing import List


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def find_next_interval(intervals: List[Interval]):
    n = len(intervals)
    res = [-1] * n
    maxStartHeap = []
    maxEndHeap = []

    for i in range(n):
        # 两个大根堆用于表示，最后一个start，最后一个end
        heappush(maxStartHeap, (-intervals[i].start, i))
        heappush(maxEndHeap, (-intervals[i].end, i))

    for _ in range(n):
        # 从最大的间隔开始遍历
        topEnd, endIndex = heappop(maxEndHeap)
        # 如果有start大于它的话
        if -maxStartHeap[0][0] >= -topEnd:
            topStart, startIndex = heappop(maxStartHeap)
            # 一直pop到不再满足条件
            while maxStartHeap and -maxStartHeap[0][0] >= -topEnd:
                topStart, startIndex = heappop(maxStartHeap)
            # 更新res
            res[endIndex] = startIndex
            # 放回最后一个满足条件的，因为它可能是上一个的答案
            heappush(maxStartHeap, (topStart, startIndex))

    return res


def main():

    result = find_next_interval(
        [Interval(2, 3), Interval(3, 4), Interval(5, 6)])
    print("Next interval indices are: " + str(result))

    result = find_next_interval(
        [Interval(3, 4), Interval(1, 5), Interval(4, 6)])
    print("Next interval indices are: " + str(result))


main()
