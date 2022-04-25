class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        dct = {']': '[', ')': '(', '}': '{'}
        stack = []

        for ch in s:
            if ch in dct:
                if not stack or stack[-1] != dct[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return len(stack) == 0


s = "){"

solution = Solution()
print(solution.isValid(s))
