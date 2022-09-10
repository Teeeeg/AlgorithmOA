from turtle import right
from typing import List


class Solution:
    # greedy
    # always use biggest to comfort biggest
    # if cannot comfort it, use the least instead

    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        sortedNums1 = sorted(nums1)

        packed = []
        for index, num in enumerate(nums2):
            packed.append((num, index))

        packed.sort(reverse=True)
        left = 0
        right = n - 1
        res = [0] * n

        for num, index in packed:
            if sortedNums1[right] > num:
                res[index] = sortedNums1[right]
                right -= 1
            else:
                res[index] = sortedNums1[left]
                left += 1

        return res