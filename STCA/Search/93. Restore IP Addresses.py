from typing import List


class Solution:

    def isValid(self, ipString: str):
        if not ipString:
            return False

        n = len(ipString)

        if n > 1 and ipString[0] == '0':
            return False

        return 0 <= int(ipString) <= 255

    def restoreIpAddressesCore(self, s: str, startIndex: int, count: int, res: List[str]):
        if count == 0:
            if self.isValid(s[startIndex:]):
                res.append(s)
            return

        for i in range(startIndex, len(s)):
            if not self.isValid(s[startIndex:i + 1]):
                continue
            # include s[i] in this segment
            # so use [: i + 1]
            self.restoreIpAddressesCore(s[:i + 1] + '.' + s[i + 1:], i + 2, count - 1, res)

    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        self.restoreIpAddressesCore(s, 0, 3, res)

        return res


s = "010010"
slt = Solution()
print(slt.restoreIpAddresses(s))