class Solution:

    def getReal(self, s):
        stack = []

        for ch in s:
            if ch == '#' and stack:
                stack.pop()
            elif ch != '#':
                stack.append(ch)

        return ''.join(stack)

    def backspaceCompare(self, s: str, t: str) -> bool:
        realS = self.getReal(s)
        realT = self.getReal(t)

        return realS == realT


s = "y#fo##f"
t = "y#f#o##f"
slt = Solution()
print(slt.backspaceCompare(s, t))