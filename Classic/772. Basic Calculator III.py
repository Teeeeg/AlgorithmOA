from typing import List

PRIORITIES = {'+': 1, '-': 1, '*': 2, '/': 2}


class Solution:

    def __init__(self) -> None:
        self.nums = [0]
        self.ops = []

    def calculateCore(self):
        if len(self.nums) < 2 or not self.ops:
            return

        rightNum = self.nums.pop()
        leftNum = self.nums.pop()
        op = self.ops.pop()
        res = 0

        if op == '+':
            res = leftNum + rightNum
        elif op == '-':
            res = leftNum - rightNum
        elif op == '*':
            res = leftNum * rightNum
        else:
            res = int(leftNum / rightNum)

        self.nums.append(res)

    def getExpression(self, s):
        expression = []
        # use None, because if ( shows, it may not have number in front of it
        n = len(s)
        i = 0

        while i < n:
            if s[i] == ' ':
                i += 1
            elif s[i] in ['+', '-', '*', '/', '(', ')']:
                expression.append(s[i])
                i += 1
            else:
                val = 0
                j = i
                while j < n and s[j].isnumeric():
                    val = val * 10 + int(s[j])
                    j += 1

                expression.append(str(val))
                i = j

        return expression

    def calculate(self, s: str) -> int:
        expression = self.getExpression(s)
        n = len(expression)

        for i in range(n):
            token = expression[i]
            if token == '(':
                self.ops.append(token)
                continue

            if token == ')':
                while self.ops and self.ops[-1] != '(':
                    self.calculateCore()
                self.ops.pop()
                continue

            if token.isnumeric():
                self.nums.append(int(token))
                continue

            if i > 0 and expression[i - 1] == '(' or expression[i - 1] == '-' or expression[i - 1] == '+':
                self.nums.append(0)

            while self.ops and self.ops[-1] != '(':
                if PRIORITIES[token] <= PRIORITIES[self.ops[-1]]:
                    self.calculateCore()
                else:
                    break
            self.ops.append(token)

        while self.ops:
            self.calculateCore()

        return int(self.nums[-1])


s = "-2+ 1"
slt = Solution()
print(slt.calculate(s))