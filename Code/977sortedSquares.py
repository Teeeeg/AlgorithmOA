from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums)-1
        res = [0] * len(nums)
        p = len(nums)-1

        while left <= right:
            if nums[left] ** 2 > nums[right] ** 2:
                res[p] = nums[left] ** 2
                left += 1
            else:
                res[p] = nums[right] ** 2
                right -= 1
            p -= 1

        return res
