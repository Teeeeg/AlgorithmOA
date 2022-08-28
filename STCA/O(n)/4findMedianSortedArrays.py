from typing import List


class Solution:
    # binary search
    # imagine inf after every list
    def findKthElement(self, nums1: List[int], nums2: List[int], index1: int, index2: int, k):
        MAX = 10**9

        # base
        if index1 == len(nums1):
            # [0, 1, 2] kth is 0 + k - 1
            return nums2[index2 + k - 1]

        if index2 == len(nums2):
            return nums1[index1 + k - 1]

        if k == 1:
            return min(nums1[index1], nums2[index2])

        # get k // 2 th in every list
        num1 = nums1[index1 + k // 2 - 1] if index1 + k // 2 - 1 < len(nums1) else MAX
        num2 = nums2[index2 + k // 2 - 1] if index2 + k // 2 - 1 < len(nums2) else MAX

        # prune smaller one
        if num1 <= num2:
            # [ :index + k // 2 - 1] will be pruned, hence new index is index1 + k // 2
            return self.findKthElement(nums1, nums2, index1 + k // 2, index2, k - k // 2)
        else:
            return self.findKthElement(nums1, nums2, index1, index2 + k // 2, k - k // 2)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        n = n1 + n2

        if n % 2:
            return self.findKthElement(nums1, nums2, 0, 0, n // 2 + 1)

        return (self.findKthElement(nums1, nums2, 0, 0, n // 2) + self.findKthElement(nums1, nums2, 0, 0, n // 2 + 1)) / 2


nums1 = [1, 2]
nums2 = [3, 4]
slt = Solution()
print(slt.findMedianSortedArrays(nums1, nums2))
