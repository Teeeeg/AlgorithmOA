class Solution:

    def removeOuterParentheses(self, s: str) -> str:
        index = -1
        res = ''

        for ch in s:
            # in case of '('
            # if stack has remains, current ch is a inside
            if ch == '(':
                if index != -1:
                    res += ch
                index += 1
            # in case of ')'
            # after pop, the stack has remains, current ch is a inside
            else:
                index -= 1
                if index > -1:
                    res += ch

        return res


slt = Solution()
print(slt.removeOuterParentheses("(()())(())"))