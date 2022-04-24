import math
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        res = -math.inf
        for i in range(n):
            for j in range(i, n):
                partialSum = sum(nums[i: j+1])
                res = max(partialSum, res)

        return res

    # 动态规划
    # 转移方程  dp[i] = max(nums[i], dp[i-1]+nums[i])
    # 依赖于dp[i-1] + nums 将nums[i]加入子序列，nums[i]表示从现在这个开始计算
    def maxSubArray1(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]

        if n == 1:
            return nums[0]

        for i in range(1, n):
            dp[i] = max(nums[i], dp[i-1]+nums[i])

        return max(dp)


nums = [-1, -2]
solution = Solution()
print(solution.maxSubArray1(nums))
