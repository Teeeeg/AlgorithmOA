from typing import List


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        left = 0

        for right in range(1, n):
            # don't forget about the index of 0
            if nums[left] != nums[right] or left == 0:
                left += 1
                nums[left] = nums[right]
            elif nums[left] == nums[right] and (left > 0 and nums[left - 1] != nums[left]):
                left += 1
                nums[left] = nums[right]

        return left + 1


nums = [1, 1, 1, 2, 2, 3]
slt = Solution()
print(slt.removeDuplicates(nums))
print(nums)