from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i] 表示到前i个数最大子数组和
        dp = [0]*n
        dp[0] = nums[0]

        for i in range(1, n):
            dp[i] = max(dp[i-1]+nums[i], nums[i])

        return max(dp)


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums1 = [5, 4, -1, 7, 8]
solution = Solution()
print(solution.maxSubArray(nums))
