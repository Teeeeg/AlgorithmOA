import math
from typing import List


class Solution:
    # 计算当前的最大乘积仅依赖于前面一个的最大或最小值
    # 因此适合使用动态规划
    # 记录最小值，因为负数的情况，大体可以认为负数乘以小的数自然大
    def maxProduct(self, nums: List[int]):
        # base case
        n = len(nums)
        if n == 1:
            return nums[0]
        # dp[0][i] 表示到i位置最大乘积
        # dp[1][i] 表示到i位置最小乘积
        dp = [[0] * n for _ in range(2)]
        # 初始化
        dp[0][0] = nums[0]
        dp[1][0] = nums[0]
        res = nums[0]

        for i in range(1, n):
            # 计算最大
            dp[0][i] = max(max(dp[0][i - 1] * nums[i], dp[1][i - 1] * nums[i]), nums[i])
            # 计算最小
            dp[1][i] = min(min(dp[0][i - 1] * nums[i], dp[1][i - 1] * nums[i]), nums[i])
            # 记录最大乘积
            res = max(res, dp[0][i], dp[1][i])

        return res


nums = [2, -1, 1, 1]
slt = Solution()
print(slt.maxProduct(nums))