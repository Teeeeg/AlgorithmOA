from heapq import heappop, heappush
from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dct = {}
        minHeap = []

        for num in arr:
            if num not in dct:
                dct[num] = 0
            dct[num] += 1

        for num, freq in dct.items():
            heappush(minHeap, (freq, num))

        while minHeap and k > 0:
            freq, _ = minHeap[0]
            if k >= freq:
                heappop(minHeap)
                k -= freq
            else:
                break

        return len(minHeap)


arr = [5, 5, 4]
k = 1
solution = Solution()
print(solution.findLeastNumOfUniqueInts(arr, k))
