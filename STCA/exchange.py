from typing import List


class Solution:

    def exchange(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 0

        for right in range(n):
            if nums[right] % 2:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

        return nums


nums = [1, 2, 3, 4, 8, 9, 11]
slt = Solution()
print(slt.exchange(nums))