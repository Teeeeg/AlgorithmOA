from typing import List


class Solution:

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 2)

        for i in range(2, n + 2):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 2])

        return dp[-1]


nums = [1, 3]
slt = Solution()
print(slt.rob(nums))