from heapq import heappop, heappush
from typing import List


class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}

        for num in nums:
            dct[num] = dct.get(num, 0) + 1

        minHeap = []

        for num, freq in dct.items():
            heappush(minHeap, (freq, num))
            if len(minHeap) > k:
                heappop(minHeap)

        return [item[1] for item in minHeap]


nums = [1, 1, 1, 2, 2, 3]
k = 2
slt = Solution()
print(slt.topKFrequent(nums, k))
