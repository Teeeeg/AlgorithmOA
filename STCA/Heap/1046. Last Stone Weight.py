from heapq import heappop, heappush
from typing import List


class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0

        maxHeap = []
        for stone in stones:
            heappush(maxHeap, -stone)

        while len(maxHeap) >= 2:
            stone1 = -heappop(maxHeap)
            stone2 = -heappop(maxHeap)

            heappush(maxHeap, stone2 - stone1)

        return -maxHeap[0]