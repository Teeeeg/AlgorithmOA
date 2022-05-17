from heapq import heappop, heappush
from typing import List


class Solution:

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        maxHeap = []
        for num in arr:
            heappush(maxHeap, -num)
            if len(maxHeap) > k:
                heappop(maxHeap)

        return [-1 * num for num in maxHeap]