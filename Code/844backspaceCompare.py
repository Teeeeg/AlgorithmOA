from typing import List


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        word1 = self.getRealWord(s)
        word2 = self.getRealWord(t)
        return word1 == word2

    def getRealWord(self, s: str):
        stack = []
        for ch in s:
            if ch == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(ch)

        return ''.join(stack)


s = "ab#c"
t = "ad#c#"
solution = Solution()
print(solution.backspaceCompare(s, t))
