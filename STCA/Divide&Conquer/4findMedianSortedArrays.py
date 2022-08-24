import math
from typing import List


class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        m = (n1 + n2) // 2 + 1
        nums = [0] * m
        i = 0
        j = 0
        k = 0

        while i < n1 and j < n2 and k < m:
            if nums1[i] <= nums2[j]:
                nums[k] = nums1[i]
                i += 1
            else:
                nums[k] = nums2[j]
                j += 1
            k += 1

        while k < m and (i < n1 or j < n2):
            if i < n1:
                nums[k] = nums1[i]
                i += 1
            else:
                nums[k] = nums2[j]
                j += 1
            k += 1

        if (n1 + n2) % 2:
            return nums[m - 1]
        else:
            return (nums[m - 1] + nums[m - 2]) / 2.0


nums1 = [1]
nums2 = []
slt = Solution()
print(slt.findMedianSortedArrays(nums1, nums2))