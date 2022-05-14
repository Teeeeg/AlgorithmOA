from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        # dp[i] 表示[0, i]连续子数组的最大和
        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1, n):
            dp[i] = max(dp[i-1]+nums[i], nums[i])

        return max(dp)


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
s = Solution()
print(s.maxSubArray(nums))
