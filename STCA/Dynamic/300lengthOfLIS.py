from typing import List


class Solution:

    def __init__(self) -> None:
        self.LIS = []

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        # opt[i] means the LIS of using nums[i] as the end
        opt = [1] * n
        res = 1
        resIndex = 0
        self.path = [-1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    opt[i] = max(opt[i], opt[j] + 1)
                    self.path[i] = j
                if opt[i] > res:
                    resIndex = i
                    res = opt[i]

        self.getLIS(nums, resIndex)

        return res

    def getLIS(self, nums: List[int], index):
        if index == -1:
            return

        self.getLIS(nums, self.path[index])
        self.LIS.append(nums[index])


nums = [7, 7, 7, 7, 7, 7, 7]
slt = Solution()
print(slt.lengthOfLIS(nums))
print(slt.LIS)