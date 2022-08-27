from typing import List


class Solution:

    def lengthOfLISCore(self, nums: List[int], index, memo):
        if index == len(nums):
            return 1

        if memo[index] != -1:
            return memo[index]

        memo[index] = 0
        for i in range(index + 1, len(nums)):
            if nums[index] >= nums[i]:
                continue

            memo[index] = max(memo[index], self.lengthOfLISCore(nums, i, memo) + 1)

        return memo[index]

    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 0
        memo = [-1] * len(nums)

        for i in range(len(nums)):
            res = max(res, self.lengthOfLISCore(nums, i, memo) + 1)

        return res


nums = [10, 9, 2, 5, 3, 7, 101, 18]
slt = Solution()
print(slt.lengthOfLIS(nums))