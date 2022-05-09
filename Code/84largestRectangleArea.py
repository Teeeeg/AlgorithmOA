from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 处理临界情况
        heights.insert(0, 0)
        heights.append(0)
        n = len(heights)
        descStack = [0]
        res = 0

        for i in range(1, n):
            while descStack and heights[descStack[-1]] > heights[i]:
                midIndex = descStack.pop()
                if descStack:
                    leftIndex = descStack[-1]
                    rightIndex = i
                    width = rightIndex-leftIndex-1
                    height = heights[midIndex]
                    area = width * height
                    res = max(res, area)
            descStack.append(i)

        return res


heights = [2, 1, 5, 6, 2, 3]
# heights = [1]
solution = Solution()
print(solution.largestRectangleArea(heights))
