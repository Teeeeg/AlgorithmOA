from typing import List


class Solution:

    def firstMissingPositive(self, nums: List[int]) -> int:
        # 归位
        n = len(nums)

        # 正数，0->1
        # 则有 nums[nums[i]-1] = nums[i] 0号位置的数字应该为1
        for i in range(n):
            # 在范围内，若不满足
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                # 交换
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(n):
            if nums[i] - 1 != i:
                return i + 1

        return n + 1


nums = [1, 4, 0, 2]
slt = Solution()
print(slt.firstMissingPositive(nums))