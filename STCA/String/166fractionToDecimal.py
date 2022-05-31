class Solution:
    # 正常模拟 长除法
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # 若可以直接被整除，直接返回
        if numerator % denominator == 0:
            return str(numerator // denominator)
        # 记录符号
        sign = -1 if numerator * denominator < 0 else 1
        n = abs(numerator)
        d = abs(denominator)
        res = []

        if sign == -1:
            res.append('-')
        # 先把整数部分算出来
        res.append(str(n // d))
        res.append('.')
        # 余数
        n %= d
        # {余数， 出现的位置（长度）}
        seen = {}
        while n:
            # 每次记录
            seen[n] = len(res)
            # 余数乘以10
            n *= 10
            res.append(str(n // d))
            n %= d
            # 若出现，则表明是循环
            if n in seen:
                index = seen[n]
                res.insert(index, '(')
                res.append(')')
                break

        return ''.join(res)


numerator = -50
denominator = 8
slt = Solution()
print(slt.fractionToDecimal(numerator, denominator))