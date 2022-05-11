class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch == '(':
                stack.append(')')
            elif ch == '[':
                stack.append(']')
            elif ch == '{':
                stack.append('}')
            elif not stack or stack[-1] != ch:
                return False
            else:
                stack.pop()

        return True if not stack else False


s = "()[]{}"
solution = Solution()
print(solution.isValid(s))
