from typing import List


class Solution:

    def findRepeatNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return nums[i]

        return -1


class Solution1:

    def findRepeatNumber(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0

        while i < n:
            if nums[i] == i:
                i += 1
                continue

            if nums[i] == nums[nums[i]]:
                return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

        return -1


nums = [3, 4, 2, 0, 0, 1]
slt = Solution1()
print(slt.findRepeatNumber(nums))