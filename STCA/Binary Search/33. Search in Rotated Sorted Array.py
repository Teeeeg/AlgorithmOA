from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1

        while left + 1 < right:
            mid = (left + right) // 2

            if nums[mid] <= nums[right]:
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid
            else:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid

        if nums[left] == target:
            return left
        if nums[right] == target:
            return right

        return -1