from typing import List


class Solution:

    def getExpressions(self, s: str) -> List[str]:
        i = 0
        res = []

        while i < len(s):
            if i < len(s) and s[i] in ['[', ']']:
                res.append(s[i])
                i += 1

            elif s[i].isalpha():
                alpha = ''
                while i < len(s) and s[i].isalpha():
                    alpha += s[i]
                    i += 1
                res.append(alpha)
            else:
                num = 0
                while i < len(s) and s[i].isnumeric():
                    num = num * 10 + int(s[i])
                    i += 1
                res.append(str(num))

        return res

    def decodeString(self, s: str) -> str:
        numStack = []
        stack = []

        expressions = self.getExpressions(s)
        for expression in expressions:
            if expression.isnumeric():
                numStack.append(int(expression))
            if expression == '[' or expression.isalpha():
                stack.append(expression)

            if expression == ']':
                word = []
                while stack[-1] != '[':
                    word.append(stack.pop())
                stack.pop()
                stack.append(''.join(word[::-1]) * numStack.pop())

        return ''.join(stack)


s = "3[a]2[bc]"
slt = Solution()
print(slt.decodeString(s))
