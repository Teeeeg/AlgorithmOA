from heapq import heappop, heappush
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHep = []

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heappush(self.minHep, val)
        if len(self.minHep) > self.k:
            heappop(self.minHep)

        return self.minHep[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
