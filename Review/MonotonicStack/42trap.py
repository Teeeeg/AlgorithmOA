from typing import List


class Solution:

    def trap(self, height: List[int]) -> int:
        n = len(height)
        monoStack = []
        res = 0

        for i in range(n):
            # pop out every height smaller than current
            # so it maintain its left right bigger than it
            while monoStack and height[monoStack[-1]] < height[i]:
                midIndex = monoStack.pop()
                if monoStack:
                    leftIndex = monoStack[-1]
                    rightIndex = i
                    h = min(height[leftIndex], height[rightIndex]) - height[midIndex]
                    area = (rightIndex - leftIndex - 1) * h
                    res += area
            monoStack.append(i)

        return res


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
slt = Solution()
print(slt.trap(height))