from typing import List


class Solution:

    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        leftSum = 0

        for i in range(n):
            if total - leftSum - nums[i] == leftSum:
                return i
            leftSum += nums[i]

        return -1


nums = [2, 1, -1]
slt = Solution()
print(slt.pivotIndex(nums))