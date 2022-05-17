from typing import List


class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0

        stack = []

        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                stack.append(int(token))
            else:
                rightNum = stack.pop()
                leftNum = stack.pop()
                if token == '+':
                    stack.append(leftNum + rightNum)
                elif token == '-':
                    stack.append(leftNum - rightNum)
                elif token == '*':
                    stack.append(leftNum * rightNum)
                elif token == '/':
                    stack.append(int(leftNum / rightNum))

        return stack[0]


tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
slt = Solution()
print(slt.evalRPN(tokens))