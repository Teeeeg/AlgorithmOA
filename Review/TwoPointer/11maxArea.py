from typing import List


class Solution:

    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        res = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            if area > res:
                res = area
            if left < right and height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return res


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
slt = Solution()
print(slt.maxArea(height))