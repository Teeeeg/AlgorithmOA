import math
from typing import List


class Solution:

    def getNum(self, nums: List[int], index):
        n = len(nums)
        if index < 0 or index > n - 1:
            return -math.inf
        return nums[index]

    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            if self.getNum(nums, mid - 1) < nums[mid] and nums[mid] > self.getNum(nums, mid + 1):
                return mid
            if nums[mid] > self.getNum(nums, mid - 1):
                left = mid + 1
            else:
                right = mid - 1

        return -1