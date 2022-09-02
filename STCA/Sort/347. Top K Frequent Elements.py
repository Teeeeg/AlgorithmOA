from heapq import heappop, heappush
from random import randint
from typing import List, Tuple


class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num2Freq = {}

        for num in nums:
            num2Freq[num] = num2Freq.get(num, 0) + 1

        minHeap = []

        for num, freq in num2Freq.items():
            heappush(minHeap, (freq, num))
            if len(minHeap) > k:
                heappop(minHeap)

        return [item[1] for item in minHeap]


class Solution1:

    def partition(self, nums: List[Tuple[int, int]], left, right):
        pivotIndex = randint(left, right)
        pivotVal = nums[pivotIndex][1]
        nums[left], nums[pivotIndex] = nums[pivotIndex], nums[left]
        l = left
        r = right

        while l < r:
            while l < r and nums[r][1] <= pivotVal:
                r -= 1
            while l < r and nums[l][1] >= pivotVal:
                l += 1

            if l < r:
                nums[l], nums[r] = nums[r], nums[l]

        nums[left], nums[l] = nums[l], nums[left]

        return l

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num2Freq = {}
        for num in nums:
            num2Freq[num] = num2Freq.get(num, 0) + 1

        items = [item for item in num2Freq.items()]
        n = len(items)
        left = 0
        right = n - 1

        index = self.partition(items, left, right)
        while index != k - 1:
            if index < k - 1:
                index = self.partition(items, index + 1, right)
            else:
                index = self.partition(items, left, index - 1)

        return [item[0] for item in items[:k]]


nums = [1, 1, 1, 2, 2, 3]
k = 2
slt = Solution1()
print(slt.topKFrequent(nums, k))
