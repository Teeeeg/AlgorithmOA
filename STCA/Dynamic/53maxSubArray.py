import math
from typing import List


class Solution:

    def __init__(self) -> None:
        self.maxSub = []

    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        # opt[i] 表示以nums[i]结尾的最大子序和
        opt = [0] * n
        opt[0] = nums[0]
        self.path = [-1] * n
        res = nums[0]
        resIndex = 0

        for i in range(1, n):
            if nums[i] > opt[i - 1] + nums[i]:
                opt[i] = nums[i]
            else:
                opt[i] = opt[i - 1] + nums[i]
                self.path[i] = 1

            if opt[i] > res:
                res = opt[i]
                resIndex = i

        self.getMaxSub(nums, resIndex)
        print(self.maxSub)

        return res

    def getMaxSub(self, nums, index):
        if self.path[index] == -1:
            self.maxSub.append(nums[index])
            return

        self.getMaxSub(nums, index - 1)
        self.maxSub.append(nums[index])


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
slt = Solution()
print(slt.maxSubArray(nums))
