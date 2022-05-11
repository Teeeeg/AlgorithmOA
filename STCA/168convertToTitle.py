class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        num = columnNumber

        while num:
            num -= 1
            ch = chr(num % 26 + ord('A'))
            res.append(ch)
            num = num // 26

        return ''.join(reversed(res))


columnNumber = 2147483647
soltuion = Solution()
print(soltuion.convertToTitle(columnNumber))
