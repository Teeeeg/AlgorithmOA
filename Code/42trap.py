from typing import List

# 双指针法


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0

        for i in range(1, n-1):
            leftHeight = height[i]
            rightHeight = height[i]

            for j in reversed(range(i+1)):
                if height[j] > leftHeight:
                    leftHeight = height[j]

            for j in range(i, n):
                if height[j] > rightHeight:
                    rightHeight = height[j]
            # 每次只计算一列的
            if leftHeight != height[i] and rightHeight != height[i]:
                area = min(leftHeight, rightHeight) - height[i]
                res += area

        return res


# 单调栈
class Solution1:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ascStack = [0]
        res = 0

        for i in range(1, n):
            # pop出所有比它小的元素
            while ascStack and height[ascStack[-1]] < height[i]:
                mid = ascStack.pop()
                if ascStack:
                    rightHeight = height[i]
                    leftHeight = height[ascStack[-1]]
                    # 选两侧较小的高度
                    h = min(leftHeight, rightHeight) - height[mid]
                    w = i - ascStack[-1] - 1
                    res += h * w
            ascStack.append(i)

        return res


# height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# height = [4, 2, 0, 3, 2, 5]
height = [5, 5, 1, 7, 1, 1, 5, 2, 7, 6]
solution = Solution1()
print(solution.trap(height))
