from typing import List


class Solution:

    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 1

        # dp[i] 表示[0, i] 最长递增子序列的长度
        dp = [1] * n
        # count[i] 表示[0, i] 最长递增子序列的个数
        count = [1] * n
        maxLen = 0
        res = 0

        for i in range(1, n):
            for j in range(i):
                # 出现递增
                if nums[i] > nums[j]:
                    # 出现长度更长的
                    if dp[i] < dp[j] + 1:
                        # 记录更长的长度
                        dp[i] = dp[j] + 1
                        # 从j更新计数
                        count[i] = count[j]
                    elif dp[i] == dp[j] + 1:
                        # 若与当前长度一致
                        # 叠加
                        count[i] += count[j]
                maxLen = max(maxLen, dp[i])
        # 最终应该统计长度为maxLen的个数
        for i in range(n):
            if dp[i] == maxLen:
                res += count[i]

        return res


nums = [1]
slt = Solution()
print(slt.findNumberOfLIS(nums))