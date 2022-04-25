class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n = columnNumber
        res = []
        while n:
            n -= 1
            ch = chr(ord('A') + n % 26)
            res.append(ch)
            n //= 26

        return ''.join(res[::-1])


columnNumber = 30
solution = Solution()
print(solution.convertToTitle(columnNumber))
