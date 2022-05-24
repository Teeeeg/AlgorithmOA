from typing import List


class Solution:

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        if n == 2:
            return max(nums)

        # dp[i] 表示考虑i个房的最大利润
        # 考虑，可能没抢也可能抢了
        # 取最大值传递就行
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            # 抢当前的则不可以考虑i-1
            # 不抢则考虑i-1
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]


nums = [1, 2, 3, 1]
slt = Solution()
print(slt.rob(nums))