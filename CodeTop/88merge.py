from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        cur = len(nums1)-1
        i1 = m
        i2 = n

        while i1 >= 0 and i2 >= 0:
            if nums1[i1] > nums2[i2]:
                nums1[cur] = nums1[i1]
                i1 -= 1
            else:
                nums1[cur] = nums2[i2]
                i2 -= 1
            cur -= 1

        while i2 >= 0:
            nums1[cur] = nums2[i2]
            i2 -= 1
            cur -= 1
