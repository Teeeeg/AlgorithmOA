class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:
        sList = list(s)
        pareStack = []

        # store the index of it
        for i in range(len(sList)):
            if sList[i] == '(':
                pareStack.append(i)
            elif sList[i] == ')':
                if pareStack and sList[pareStack[-1]] == '(':
                    pareStack.pop()
                else:
                    sList[i] = ''
            else:
                continue

        # remaining index is the ones to delete
        for index in pareStack:
            sList[index] = ''

        return ''.join(sList)


s = "lee(t(c)o)de)"
slt = Solution()
print(slt.minRemoveToMakeValid(s))