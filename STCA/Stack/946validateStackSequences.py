from typing import List


class Solution:
    # 贪心
    # 按顺序往压栈

    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        index = 0

        for num in pushed:
            stack.append(num)
            # 若栈顶与当前值相同则pop
            while stack and stack[-1] == popped[index]:
                stack.pop()
                # 维护index
                index += 1
        # 最后index 会变成n
        return index == len(popped)


pushed = [1, 2, 3, 4, 5]
popped = [4, 5, 3, 2, 1]
slt = Solution()
print(slt.validateStackSequences(pushed, popped))