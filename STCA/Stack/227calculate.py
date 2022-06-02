class Solution:

    def __init__(self) -> None:
        self.nums = []
        self.ops = []

    def calculate(self, s: str) -> int:
        priorities = {'+': 1, '-': 1, '*': 2, '/': 2}

        s = s.replace(' ', '')
        n = len(s)
        i = 0

        while i < n:
            if s[i].isdigit():
                num = 0
                j = i
                while j < n and s[j].isdigit():
                    num = num * 10 + int(s[j])
                    j += 1
                i = j
                self.nums.append(num)
            else:
                curOp = s[i]
                while self.ops and priorities[self.ops[-1]] >= priorities[curOp]:
                    self.calculateCore()
                self.ops.append(curOp)
                i += 1

        while self.ops:
            self.calculateCore()

        return self.nums[-1]

    def calculateCore(self):
        if len(self.nums) < 2:
            return

        if not self.ops:
            return

        op = self.ops.pop()
        rightNum = self.nums.pop()
        leftNum = self.nums.pop()
        res = 0

        if op == '+':
            res = leftNum + rightNum
        if op == '-':
            res = leftNum - rightNum
        if op == '*':
            res = leftNum * rightNum
        if op == '/':
            res = leftNum // rightNum

        self.nums.append(res)


s = "1+1+1"
slt = Solution()
print(slt.calculate(s))