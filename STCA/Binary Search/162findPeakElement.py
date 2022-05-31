import math
from typing import List


class Solution:
    # 二分搜索
    # 解决题目头和为负无穷
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
            # 如果当前递增
            if nums[mid] > self.getNum(nums, mid - 1):
                left = mid + 1
            else:
                right = mid - 1

        return -1


nums = [1, 2, 3, 1]
slt = Solution()
print(slt.findPeakElement(nums))