from typing import List


class Solution:
    # 顺着递增的走
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = 0, n-1

        while left < right:
            mid = (left+right) >> 1

            # 升序，则结果一定在mid之后
            if arr[mid] < arr[mid+1]:
                left = mid+1
            # 降序，则结果一定是mid或在mid之前
            else:
                right = mid

        return left


arr = []
solution = Solution()
print(solution.peakIndexInMountainArray(arr))
