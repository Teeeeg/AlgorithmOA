class Solution:

    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber:
            columnNumber -= 1
            cur = chr(ord('A') + columnNumber % 26)
            res.append(cur)
            columnNumber //= 26
        return ''.join(res[::-1])


columnNumber = 28
slt = Solution()
print(slt.convertToTitle(columnNumber))