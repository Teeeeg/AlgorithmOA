from collections import deque


class Solution:

    def convertToTitle(self, columnNumber: int) -> str:
        res = deque()

        while columnNumber > 0:
            pivot = columnNumber % 26
            # 26 is the index of z
            if pivot == 0:
                # z shouldbe get from higher 26 + 0
                pivot = 26
                columnNumber -= 26
            columnNumber //= 26
            res.appendleft(chr(ord('A') + pivot - 1))

        return ''.join(res)


columnNumber = 701
slt = Solution()
print(slt.convertToTitle(columnNumber))