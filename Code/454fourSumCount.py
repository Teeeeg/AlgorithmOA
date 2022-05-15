from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        dct = {}
        res = 0

        for i in range(n):
            for j in range(n):
                total = nums1[i] + nums2[j]
                dct[total] = dct.get(total, 0)+1

        for i in range(n):
            for j in range(n):
                key = -nums3[i]-nums4[j]
                res += dct.get(key, 0)

        return res
