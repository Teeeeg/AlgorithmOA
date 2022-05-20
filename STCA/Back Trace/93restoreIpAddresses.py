from typing import List


class Solution:

    def isValid(self, s: str, start, end):
        # 判断输入是否有效
        if start > end:
            return False
        # 若该段为0xx
        if s[start] == '0' and start != end:
            return False

        num = 0
        # 遍历若有非法字段
        for i in range(start, end + 1):
            if not s[i].isdigit():
                return False
            else:
                num = num * 10 + int(s[i])
        # 最终值的大小不在0-255之间
        if not 0 <= num <= 255:
            return False

        return True

    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        self.restoreIpAddressesCore(s, 0, res, 0)
        return res

    def restoreIpAddressesCore(self, s: str, startIndex, res: List[str], sepCount):
        # 四段只需要加三个点
        if sepCount == 3:
            if self.isValid(s, startIndex, len(s) - 1):
                res.append(s)
            return

        for i in range(startIndex, len(s)):
            if self.isValid(s, startIndex, i):
                # 加 ‘.’
                s = s[:i + 1] + '.' + s[i + 1:]
                # 注意i+2，因为添加一个.之后，下一个字符应该是i+2
                self.restoreIpAddressesCore(s, i + 2, res, sepCount + 1)
                # 回溯
                s = s[:i + 1] + s[i + 2:]
            else:
                break


s = "101023"
slt = Solution()
print(slt.restoreIpAddresses(s))