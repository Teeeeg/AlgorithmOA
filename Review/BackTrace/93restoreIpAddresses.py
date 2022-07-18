from typing import List


class Solution:

    def isValid(self, s, left, right):
        if left > right:
            return False

        if s[left] == '0' and left != right:
            return False

        num = 0
        for i in range(left, right + 1):
            ch = s[i]
            if not '0' <= ch <= '9':
                return False
            num = num * 10 + int(ch)

        return 0 <= num <= 255

    def restoreIpAddressesCore(self, s, startIndex, count, res):
        if count == 3:
            if self.isValid(s, startIndex, len(s) - 1):
                res.append(s[:])
                return

        for i in range(startIndex, len(s)):
            if self.isValid(s, startIndex, i):
                s = s[:i + 1] + '.' + s[i + 1:]
                self.restoreIpAddressesCore(s, i + 2, count + 1, res)
                s = s[:i + 1] + s[i + 2:]

    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        self.restoreIpAddressesCore(s, 0, 0, res)
        return res


s = '25525511135'
slt = Solution()
print(slt.restoreIpAddresses(s))