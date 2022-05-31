from typing import List


class Solution:
    # 字符串想家
    def addString(self, num1: str, num2: str) -> str:
        n1 = len(num1)
        n2 = len(num2)
        res = ''

        i1 = n1 - 1
        i2 = n2 - 1
        carry = 0

        while i1 >= 0 or i2 >= 0:
            digit1 = int(num1[i1]) if i1 >= 0 else 0
            digit2 = int(num2[i2]) if i2 >= 0 else 0
            total = digit1 + digit2 + carry
            carry = total // 10
            res += str(total % 10)
            i1 -= 1
            i2 -= 1
        # 最后判断是否有carry
        if carry:
            res += '1'

        return ''.join(reversed(res))

    # 每一位进位算进去
    # 12, 29, 15 -> 2, 0, 8, 2
    # 倒过来进位计算
    # 最后也要倒着返回
    def carrySolver(self, nums: List[str]):
        res = []
        carry = 0

        for num in nums:
            total = carry + int(num)
            res.append(str(total % 10))
            carry = total // 10
        if carry:
            res.append(str(carry))

        return ''.join(reversed(res))

    def multiply(self, num1: str, num2: str) -> str:
        # corner
        if num1 == '0' or num2 == '0':
            return '0'
        # 选一个长的当num1
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        n = len(num2)
        pre = []
        # 大体思路
        # 每个位置乘以当前位
        # 要按位乘以10
        for i in range(n - 1, -1, -1):
            # 记录第几位
            offset = 10**(n - i - 1)
            multi = []
            for j in range(len(num1)):
                cur = int(num1[j]) * int(num2[i]) * offset
                multi.append(cur)
            # 倒序传入
            cur = self.carrySolver(reversed(multi))  # type: ignore
            if pre:
                # 两个两个相加
                cur = self.addString(''.join(pre), ''.join(cur))
            pre = cur

        return ''.join(pre)


num1 = "123456789"
num2 = "987654321"
slt = Solution()
print(slt.multiply(num1, num2))
