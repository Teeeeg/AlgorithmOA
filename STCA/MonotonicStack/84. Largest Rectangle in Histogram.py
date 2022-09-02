from typing import List


class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0

        n = len(heights)
        monoStack = []
        res = 0

        for i in range(n + 1):
            curHeight = -1
            if i != n:
                curHeight = heights[i]

            while monoStack and heights[monoStack[-1]] >= curHeight:
                height = heights[monoStack.pop()]
                leftIndex = monoStack[-1] if monoStack else -1
                rightIndex = i
                res = max(res, (rightIndex - leftIndex - 1) * height)

            monoStack.append(i)

        return res