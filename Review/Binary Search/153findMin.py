from typing import List


class Solution:

    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1

        while left <= right:
            mid = left + (right - left) // 2
            # 防止越界
            # 分别两种应该返回的情况
            if right > mid and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if left < mid and nums[mid] < nums[mid - 1]:
                return nums[mid]
            # 若left到mid之间有序
            # 则缩小范围到[mid+1, right]
            if nums[right] > nums[mid]:
                right = mid - 1
            # mid到right上有序
            # 缩小到[left, mid-1]
            else:
                left = mid + 1
        # 若循环结束，说明没有旋转，则返回第一个
        return nums[0]