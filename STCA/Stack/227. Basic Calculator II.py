class Solution:

    def __init__(self) -> None:
        self.nums = []
        self.ops = []

    def calculateCore(self):
        if len(self.nums) < 2 or not self.ops:
            return

        rightNum = self.nums.pop()
        leftNum = self.nums.pop()
        op = self.ops.pop()

        if op == '+':
            self.nums.append(leftNum + rightNum)
        if op == '-':
            self.nums.append(leftNum - rightNum)
        if op == '*':
            self.nums.append(leftNum * rightNum)
        if op == '/':
            self.nums.append(int(leftNum / rightNum))

    def getExpression(self, s: str):
        res = []
        i = 0

        while i < len(s):
            if s[i] == ' ':
                i += 1
            elif s[i] in ['+', '-', '*', '/']:
                res.append(s[i])
                i += 1
            else:
                num = 0
                while i < len(s) and s[i].isnumeric():
                    num = num * 10 + int(s[i])
                    i += 1

                res.append(str(num))

        return res

    def calculate(self, s: str) -> int:
        priorities = {'+': 1, '-': 1, '*': 2, '/': 2}
        expressions = self.getExpression(s)

        for expression in expressions:
            if expression in ['+', '-', '*', '/']:
                while self.ops and priorities[self.ops[-1]] >= priorities[expression]:
                    self.calculateCore()
                self.ops.append(expression)
            else:
                self.nums.append(int(expression))

        while self.ops:
            self.calculateCore()

        return self.nums[0]


s = "1*2-3/4+5*6-7*8+9/10"
slt = Solution()
print(slt.calculate(s))