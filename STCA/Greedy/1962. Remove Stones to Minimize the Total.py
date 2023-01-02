from heapq import heappop, heappush
from typing import List


class Solution:

    def minStoneSum(self, piles: List[int], k: int) -> int:
        maxHeap = []

        for pile in piles:
            heappush(maxHeap, -pile)

        while maxHeap and k > 0:
            cur = -heappop(maxHeap)
            cur -= cur // 2
            k -= 1

            if cur > 0:
                heappush(maxHeap, -cur)

        return -sum(maxHeap)


piles = [4, 3, 6, 7]
k = 3
slt = Solution()
print(slt.minStoneSum(piles, k))