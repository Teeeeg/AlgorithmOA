from typing import List


class Solution:

    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1

        while left + 1 < right and nums[left] == nums[right]:
            right -= 1

        while left + 1 < right:
            mid = (left + right) // 2

            if nums[mid] < nums[right]:
                right = mid
            # beside 153, if equal it needs to shrink
            elif nums[mid] == nums[right]:
                right -= 1
            else:
                left = mid

        return min(nums[left], nums[right])
