from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        left, right = 0, n-k-1

        while left <= right:
            mid = (left+right) >> 1
            dist_left = x-arr[mid]
            dist_right = arr[mid+k]-x

            if dist_left > dist_right:
                left = mid+1
            else:
                right = mid-1

        return arr[left: left+k]


arr = [1, 2, 3, 4, 5]
k = 4
x = 3
solution = Solution()
print(solution.findClosestElements(arr, k, x))
