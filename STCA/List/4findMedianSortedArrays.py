class Solution:

    def findMedianSortedArraysCore(self, nums1, nums2, k):
        # nums2 保持为长度小一点的
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        # base
        if not nums2:
            return nums1[k - 1]

        # base
        if k == 1:
            return min(nums1[0], nums2[0])

        # 可能从长的传递过来的，防止越界
        # 下一段
        t = min(k // 2, len(nums2))
        if nums1[t - 1] > nums2[t - 1]:
            return self.findMedianSortedArraysCore(nums1, nums2[t:], k - t)
        else:
            return self.findMedianSortedArraysCore(nums1[t:], nums2, k - t)

    def findMedianSortedArrays(self, nums1, nums2):
        k1 = (len(nums1) + len(nums2) + 1) // 2
        k2 = (len(nums1) + len(nums2) + 2) // 2

        res1 = self.findMedianSortedArraysCore(nums1, nums2, k1)
        res2 = self.findMedianSortedArraysCore(nums1, nums2, k2)

        return (res1 + res2) / 2


nums1 = [1, 3]
nums2 = [2]
slt = Solution()
print(slt.findMedianSortedArrays(nums1, nums2))