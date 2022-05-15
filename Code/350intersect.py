from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dct = [0]*10001
        res = []

        for num in nums1:
            dct[num] += 1

        for num in nums2:
            if dct[num] > 0:
                res.append(num)
                dct[num] -= 1

        return res


class Solution1:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = len(nums1)
        n2 = len(nums2)
        nums1.sort()
        nums2.sort()

        i1 = 0
        i2 = 0
        res = []

        while i1 < n1 and i2 < n2:
            if nums1[i1] < nums2[i2]:
                i1 += 1
            elif nums1[i1] > nums2[i2]:
                i2 += 1
            else:
                res.append(nums1[i1])
                i1 += 1
                i2 += 1

        return res


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
slt = Solution()
slt1 = Solution1()
print(slt.intersect(nums1, nums2))
print(slt1.intersect(nums1, nums2))
