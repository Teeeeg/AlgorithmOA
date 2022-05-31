from typing import List


class Solution:

    def lengthOfLIS(self, nums: List[int]):
        n = len(nums)
        # dp[i] 表示 [0-i] 最长递增字序列的长度
        # 初始化，每个自己为1
        dp = [1] * n
        # 记录如何传递的
        # -1 表示没有传递
        sources = [-1] * n
        res = 1

        for i in range(1, n):
            for j in range(i):
                # 与i之前的进行对比
                if nums[i] > nums[j]:
                    # 若递增，则更新
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        sources[i] = j
            res = max(res, dp[i])

        tails = []
        # 记录递推之后，最长子序列的最后一个下标
        # 可能有多个
        for i in range(n):
            if dp[i] == res:
                tails.append(i)

        steps = []
        # 通过sources 记录每一步
        for k in tails:
            tmp = []
            while k >= 0:
                tmp.append(nums[k])
                k = sources[k]
            steps.append(list(reversed(tmp)))

        return steps


nums = [10, 9, 2, 5, 3, 7, 101, 18]
slt = Solution()
print(slt.lengthOfLIS(nums))