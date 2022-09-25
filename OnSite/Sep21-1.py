# n = int(input())
# ipStrings = [x for x in input()]


class Solution:

    def isV7(self, queryIP: str):
        arr = queryIP.split('.')

        if len(arr) != 7:
            return False

        for index, part in enumerate(arr):
            if not part:
                if index == 0 or index == 6:
                    return False
                else:
                    continue

            if part and part[0] == '0' and len(part) > 1:
                return False

            num = 0
            for digit in part:
                if not digit.isnumeric():
                    return False
                else:
                    num = num * 10 + int(digit)
            if not 0 <= num <= 255:
                return False

        return True

    def validIPAddress(self, queryIP: str):
        if self.isV7(queryIP):
            return True
        return False

    def toInteger(self, queryIP):
        arr = queryIP.split('.')

        # num = 0

        # for part in arr[:: -1]:

        pass

    def solve(self, ipStrings):
        for ipStr in ipStrings:
            if not self.validIPAddress(ipStr):
                print('-1')
        else:
            pass


slt = Solution()
print(slt.validIPAddress('1.0.0....2'))
