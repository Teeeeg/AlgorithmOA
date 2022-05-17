from typing import List


class Solution:

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = []
        res = []

        for num in nums1:
            if num not in st:
                st.append(num)

        for num in nums2:
            if num in st and num not in res:
                res.append(num)

        return res