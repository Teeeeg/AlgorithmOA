from heapq import heappop, heappush
from typing import List


class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minHeap = []
        dct = {}

        for num in nums:
            dct[num] = dct.get(num, 0) + 1

        for key, value in dct.items():
            data = (value, key)
            if len(minHeap) < k:
                heappush(minHeap, data)
            else:
                if data[0] > minHeap[0][0]:
                    heappop(minHeap)
                    heappush(minHeap, data)

        res = []
        for data in minHeap:
            res.append(data[1])

        return res


nums = [4, 1, -1, 2, -1, 2, 3]
k = 2
slt = Solution()
print(slt.topKFrequent(nums, k))
