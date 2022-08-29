from typing import List


class Solution:

    def maxCoins(self, nums: List[int]) -> int:
        nums = [1, *nums, 1]
        n = len(nums)

        opt = [[0] * n for _ in range(n)]

        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                for k in range(i + 1, j):
                    # bubble (i, k) and (k, j)
                    opt[i][j] = max(opt[i][j], opt[i][k] + opt[k][j] + nums[i] * nums[k] * nums[j])

        return opt[0][n - 1]


nums = [3, 1, 5, 8]
slt = Solution()
print(slt.maxCoins(nums))