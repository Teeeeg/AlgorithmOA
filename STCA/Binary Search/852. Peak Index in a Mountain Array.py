from typing import List


class Solution:

    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left = 0
        right = n - 1

        while left + 1 < right:
            mid = (left + right) // 2

            if arr[mid] < arr[mid + 1]:
                left = mid
            else:
                right = mid

        if arr[left] < arr[right]:
            return right

        return left