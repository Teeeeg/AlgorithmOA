from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        left = 1

        for right in range(1, n):
            if nums[right-1] != nums[right]:
                nums[left] = nums[right]
                left += 1

        return left


nums = [1, 1, 2]
s = Solution()
print(s.removeDuplicates(nums))
