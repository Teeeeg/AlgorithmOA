from typing import List


class Solution:

    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        if not nums1 or not nums2:
            return 0

        n1 = len(nums1)
        n2 = len(nums2)
        # opt[i][j] is the common subsequence length of nums[0: i] and nums[0: j]
        opt = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                context = 1 if nums1[i - 1] == nums2[j - 1] else 0
                opt[i][j] = max(opt[i - 1][j], opt[i][j - 1], opt[i - 1][j - 1] + context)

        return opt[-1][-1]
