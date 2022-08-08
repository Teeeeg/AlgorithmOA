from typing import List


class Solution:

    def __init__(self) -> None:
        self.pathVal = []

    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        self.path = [-1] * n
        opt = [[0] * n for _ in range(2)]
        opt[0][0] = nums[0]
        opt[1][0] = nums[0]

        res = nums[0]
        resIndex = 0

        for i in range(1, n):
            opt[0][i] = nums[i]
            if opt[0][i] < opt[0][i - 1] * nums[i]:
                opt[0][i] = opt[0][i - 1] * nums[i]
                self.path[i] = 1
            if opt[0][i] < opt[1][i - 1] * nums[i]:
                opt[0][i] = opt[1][i - 1] * nums[i]
                self.path[i] = 1

            opt[1][i] = nums[i]
            if opt[1][i] > opt[0][i - 1] * nums[i]:
                opt[1][i] = opt[0][i - 1] * nums[i]
                self.path[i] = 1
            if opt[1][i] > opt[1][i - 1] * nums[i]:
                opt[1][i] = opt[1][i - 1] * nums[i]
                self.path[i] = 1

            if opt[0][i] > res:
                res = opt[0][i]
                resIndex = i
            if opt[1][i] > res:
                res = opt[1][i]
                resIndex = i

        self.getMaxProduct(nums, resIndex)
        print(self.pathVal)

        return res

    def getMaxProduct(self, nums, index):
        if self.path[index] == -1:
            self.pathVal.append(nums[index])
            return

        self.getMaxProduct(nums, index - 1)
        self.pathVal.append(nums[index])


nums = [2, 3, -2, 4]
slt = Solution()
print(slt.maxProduct(nums))