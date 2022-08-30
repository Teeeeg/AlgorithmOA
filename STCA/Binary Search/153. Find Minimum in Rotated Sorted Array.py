from typing import List


class Solution:

    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1

        while left + 1 < right:
            mid = (left + right) // 2

            # it is always a rotated arr
            # satisfied left arr of cliff bigger than rightest num
            #           right arr of cliff smaller or equal than rightest num
            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid

        return min(nums[left], nums[right])