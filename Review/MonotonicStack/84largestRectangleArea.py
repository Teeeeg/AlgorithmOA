from typing import List


class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        # insert 0s to both end
        heights.insert(0, 0)
        heights.append(0)
        n = len(heights)
        descStack = [0]
        res = 0

        for i in range(1, n):
            while descStack and heights[descStack[-1]] > heights[i]:
                # midIndex is the height
                # because in the front or the back is all bigger than it
                # in the front, monoStack pops out all the bigger
                # in th back, a smaller one trigger this while
                midIndex = descStack.pop()
                if descStack:
                    leftIndex = descStack[-1]
                    rightIndex = i
                    width = rightIndex - leftIndex - 1
                    height = heights[midIndex]
                    area = width * height
                    res = max(res, area)
            descStack.append(i)

        return res


heights = [2, 3, 1, 2]
slt = Solution()
print(slt.largestRectangleArea(heights))