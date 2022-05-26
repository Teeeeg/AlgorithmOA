class Solution:

    def decodeString(self, s: str) -> str:
        stack = []
        word = ''
        num = 0

        for ch in s:
            if ch.isdigit():
                # 可能不止一位数
                num = int(ch) + num * 10
            elif ch == '[':
                # 如果为[, 则将当前的答案和次数入栈
                # s = "abc3[cd]xyz"
                # 入栈(abc, 3)
                stack.append((num, word))
                # 置空word和num
                # 表明开始遍历[]的内容
                word = ''
                num = 0
            elif ch == ']':
                # 如果为]
                # 先从栈顶获得其乘的次数再加上之前的答案
                top = stack.pop()
                # 此时word为[]的内容
                word = top[1] + top[0] * word
            else:
                # 若是字符则直接记录进word
                word += ch

        return word


s = '100[leetcode]'
slt = Solution()
print(slt.decodeString(s))