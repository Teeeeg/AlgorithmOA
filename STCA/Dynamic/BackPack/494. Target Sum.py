from typing import List


class Solution:
    # just like a 0/1 backpack

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if (total - target) % 2 or (total - target < 0):
            return 0

        n = (total - target) // 2

        opt = [0] * (n + 1)
        opt[0] = 1

        for num in nums:
            for i in range(n, num - 1, -1):
                opt[i] += opt[i - num]

        return opt[-1]


nums = [1]
target = 1
slt = Solution()
print(slt.findTargetSumWays(nums, target))
