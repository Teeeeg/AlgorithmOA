import math
from typing import List


class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [[0] * n for _ in range(2)]
        dp[0][0] = nums[0]
        dp[1][0] = nums[0]

        res = nums[0]

        for i in range(1, n):
            dp[0][i] = max(dp[0][i - 1] * nums[i], nums[i], dp[1][i - 1] * nums[i])
            dp[1][i] = min(dp[1][i - 1] * nums[i], nums[i], dp[0][i - 1] * nums[i])

            res = max(dp[0][i], dp[1][i], res)

        return res


nums = [-2, 3, -4]
slt = Solution()
print(slt.maxProduct(nums))