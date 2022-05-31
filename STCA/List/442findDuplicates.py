from typing import List


class Solution:

    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []

        for i in range(n):
            # 对于nums[i] 应该放在 nums[i] - 1这个位置
            # 因此不断交换直到归位
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i, num in enumerate(nums):
            if num != i + 1:
                res.append(num)

        return res


nums = [4, 3, 2, 7, 8, 2, 3, 1]
slt = Solution()
print(slt.findDuplicates(nums))