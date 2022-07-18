class Solution:

    def __init__(self) -> None:
        self.nums = []
        self.ops = []

    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        n = len(s)
        # 每个计算符的优先级
        priorities = {'+': 1, '-': 1, '*': 2, '/': 2}
        i = 0

        while i < n:
            ch = s[i]
            # 为左括号则直接添加
            if ch == '(':
                self.ops.append(ch)
                i += 1
            # 如果为右括号，计算到左括号之前
            elif ch == ')':
                while self.ops:
                    # 计算到左括号之前
                    if self.ops[-1] != '(':
                        self.calculateCore()
                    else:
                        self.ops.pop()
                        break
                i += 1
            else:
                # 若为数字
                if ch.isnumeric():
                    num = 0
                    j = i
                    # 多位数字，
                    while j < n and s[j].isnumeric():
                        num = num * 10 + int(s[j])
                        j += 1
                    i = j
                    self.nums.append(num)
                else:
                    # 是运算符号
                    # 处理括号里第一个元素为运算符的情况
                    # 若上一个为+，- ， 添加0为保证0-和0+
                    # if i > 0 and s[i - 1] == '(' or s[i - 1] == '-' or s[i - 1] == '+':
                    #     self.nums.append(0)
                    # 一直往前计算到'('
                    while self.ops and self.ops[-1] != '(':
                        # 若当前运算符的优先较小，则把之前的都计算一下
                        op = self.ops[-1]
                        if priorities[op] >= priorities[ch]:
                            self.calculateCore()
                        else:
                            break
                    i += 1
                    self.ops.append(ch)
        # 若最后还有运算符
        # 处理
        while self.ops:
            self.calculateCore()

        return self.nums[-1]

    def calculateCore(self):
        if not self.nums or len(self.nums) < 2:
            return

        if not self.ops:
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
        elif op == '/':
            res = int(leftNum / rightNum)

        self.nums.append(res)  # type: ignore


s = "(0-3)/4"
slt = Solution()
print(slt.calculate(s))
