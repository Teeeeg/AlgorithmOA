from typing import List


class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # use opt to record the minmal num of i length substring
        opt = [10**9] * (n + 1)
        # initialize
        # set 0 to -10**9, so every new num will go to 1 first
        opt[0] = -10**9
        res = 0

        for i in range(n):
            index = self.getGTE(opt, nums[i])
            res = max(res, index)
            opt[index] = nums[i]

        return res

    def getGTE(self, nums, target):
        n = len(nums)
        left = 0
        right = n - 1
        # res = -1

        while left <= right:
            mid = (left + right) >> 1

            if nums[mid] == target:
                return mid

            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return left


nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
slt = Solution()
print(slt.lengthOfLIS(nums))