from typing import List


class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        sums = [0] * (n + 1)
        prefixMin = sums[0]
        res = -(2 << 31)

        for i in range(n):
            sums[i + 1] = sums[i] + nums[i]
            res = max(res, sums[i + 1] - prefixMin)
            prefixMin = min(prefixMin, sums[i + 1])

        return res


class Solution1:

    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i] 表示以nums[i]结尾的最大和
        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])

        return max(dp)


nums = [-1]
slt = Solution1()
print(slt.maxSubArray(nums))