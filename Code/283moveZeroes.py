from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        left = 0
        for right in range(n):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1


nums = [2, 1]
solution = Solution()
solution.moveZeroes(nums)
print(nums)
