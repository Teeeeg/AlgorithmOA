from heapq import heappop, heappush
import math


def find_smallest_range(lists):
    minHeap = []
    res = [-math.inf, math.inf]
    curMax = -math.inf

    for i, l in enumerate(lists):
        curMax = max(curMax, l[0])
        heappush(minHeap, (l[0], 0, i))

    while len(minHeap) == len(lists):
        element, eIndex, lIndex = heappop(minHeap)

        if curMax-element < res[1]-res[0]:
            res = [element, curMax]

        if eIndex + 1 < len(lists[lIndex]):
            heappush(minHeap, (lists[lIndex][eIndex+1], eIndex+1, lIndex))

            curMax = max(curMax, lists[lIndex][eIndex+1])

    return res


def main():
    print("Smallest range is: " +
          str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]])))


main()
