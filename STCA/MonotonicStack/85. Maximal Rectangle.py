from typing import List


class Solution:

    def modifyHeight(self, matrix: List[List[str]], heights: List[int], rowIndex):
        n = len(heights)

        for colIndex in range(n):
            if matrix[rowIndex][colIndex] == '0':
                heights[colIndex] = 0
            else:
                heights[colIndex] += 1

    def getCurMaxArea(self, heights: List[int]):
        res = 0
        monoStack = []

        for i in range(len(heights) + 1):
            height = -1
            if i != len(heights):
                height = heights[i]
            while monoStack and heights[monoStack[-1]] >= height:
                curHeight = heights[monoStack.pop()]
                leftIndex = monoStack[-1] if monoStack else -1
                rightIndex = i
                res = max(res, (rightIndex - leftIndex - 1) * curHeight)
            monoStack.append(i)

        return res

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m = len(matrix)
        n = len(matrix[0])
        heights = [0] * n
        res = 0

        for rowIndex in range(m):
            self.modifyHeight(matrix, heights, rowIndex)
            res = max(res, self.getCurMaxArea(heights))

        return res


matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]

slt = Solution()
print(slt.maximalRectangle(matrix))