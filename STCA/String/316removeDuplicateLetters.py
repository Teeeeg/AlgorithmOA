from collections import Counter


class Solution:

    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        stack = []

        for ch in s:
            if ch not in stack:
                # 若前面的字符字典序大于当前的
                # 且前一个字符还有多余的，则可以被pop
                while stack and counter[stack[-1]] > 0 and stack[-1] > ch:
                    stack.pop()
                stack.append(ch)
            # 添加完成后 当前字符的数量-1
            counter[ch] -= 1

        return ''.join(stack)


s = "bcabc"
slt = Solution()
print(slt.removeDuplicateLetters(s))