from heapq import heappop, heappush
from typing import List


class Solution1:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        minHeap = []

        for i in range(n):
            heappush(minHeap, nums[i])
            if i >= k:
                heappop(minHeap)

        return minHeap[0]


class Solution:

    def partition(self, nums: List[int], left, right):
        pivotVal = nums[left]
        l = left
        r = right

        while l < r:
            while l < r and nums[r] <= pivotVal:
                r -= 1
            while l < r and nums[l] >= pivotVal:
                l += 1

            if l < r:
                nums[l], nums[r] = nums[r], nums[l]
        nums[left], nums[l] = nums[l], nums[left]

        return l

    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1

        while True:
            index = self.partition(nums, left, right)
            if index == k - 1:
                return nums[index]
            elif index < k - 1:
                left = index + 1
            else:
                right = index - 1
