from typing import List


class Solution:

    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1

        while left <= right:
            mid = left + (right - left) // 2

            if right > mid and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if left < mid and nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[right] > nums[mid]:
                right = mid - 1
            elif nums[right] == nums[mid]:
                right -= 1
            else:
                left = mid + 1
        return nums[0]


nums = [3, 3, 3, 1, 2, 2, 2, 2, 2, 2]
slt = Solution()
print(slt.findMin(nums))