import math
from typing import List


class Solution:

    def findLength(self, nums1: List[int], nums2: List[int]):
        n1 = len(nums1)
        n2 = len(nums2)

        # dp[i][j] 表示1中下标为i-1, 2中下标为j-1的 最长重复数组长度
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        res = -math.inf

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    # 若当前值相等，由他们位置互相减一得到的值递推过来
                    dp[i][j] = dp[i - 1][j - 1] + 1
                res = max(res, dp[i][j])

        return res

        # 初始化


nums1 = [0, 0, 0, 0, 0]
nums2 = [0, 0, 0, 0, 0]
slt = Solution()
print(slt.findLength(nums1, nums2))
