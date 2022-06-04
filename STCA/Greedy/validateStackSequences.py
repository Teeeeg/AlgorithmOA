from typing import List


class Solution:

    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(pushed)
        stack = []
        index = 0

        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[index]:
                stack.pop()
                index += 1

        return index == n
