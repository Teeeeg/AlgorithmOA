from typing import List


class Solution:

    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1

        while left + 1 < right:
            mid = (left + right) // 2

            if nums[mid - 1] > nums[mid]:
                right = mid
            elif nums[mid] < nums[mid + 1]:
                left = mid
            else:
                return mid

        if nums[left] > nums[right]:
            return left
        return right