class Solution:

    def isV4(self, queryIP: str):
        arr = queryIP.split('.')
        # 若长度没有4返回
        if len(arr) != 4:
            return False
        # 每一个片段
        for part in arr:
            # 若遇到片段为空
            if not part:
                return False
            # 首位不为0
            if part and part[0] == '0' and len(part) > 1:
                return False

            num = 0
            # 遍历片段
            for digit in part:
                # 非法字符就返回
                if not digit.isnumeric():
                    return False
                else:
                    # 统计值
                    num = num * 10 + int(digit)
            # 最终值不为0～255
            if not 0 <= num <= 255:
                return False

        return True

    def isV6(self, queryIP: str):
        arr = queryIP.split(':')
        # 片段总数不为8则返回
        if len(arr) != 8:
            return False
        # 处理每一个片段
        for part in arr:
            # 片段为空
            if not part:
                return False
            # 每个片段长度大于4了
            if len(part) > 4:
                return False
            for digit in part:
                # 是否合法
                if not 'a' <= digit <= 'f' and not 'A' <= digit <= 'F' and not digit.isnumeric():
                    return False
        return True

    def validIPAddress(self, queryIP: str) -> str:
        if self.isV4(queryIP):
            return 'IPv4'
        if self.isV6(queryIP):
            return 'IPv6'
        return 'Neither'


slt = Solution()
print(slt.validIPAddress('1.0.1.'))