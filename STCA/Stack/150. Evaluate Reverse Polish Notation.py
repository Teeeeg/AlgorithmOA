from typing import List

OPS = ['+', '-', '*', '/']


class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in OPS:
                stack.append(int(token))
                continue

            rightDigit = stack.pop()
            leftDigit = stack.pop()

            if token == '+':
                stack.append(leftDigit + rightDigit)
            elif token == '-':
                stack.append(leftDigit - rightDigit)
            elif token == '*':
                stack.append(leftDigit * rightDigit)
            else:
                stack.append(int(leftDigit / rightDigit))

        return stack[-1]


tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
slt = Solution()
print(slt.evalRPN(tokens))
