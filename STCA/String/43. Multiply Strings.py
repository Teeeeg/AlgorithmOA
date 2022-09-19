from typing import List


class Solution:

    def carrySovler(self, digits: List[int]):
        carry = 0
        res = []
        for digit in digits:
            actualDigit = (digit + carry) % 10
            carry = (digit + carry) // 10
            res.append(str(actualDigit))

        if carry:
            res.append(str(carry))

        return ''.join(res[::-1])

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        allDigits = []
        mod = 1
        for digit1 in num1[::-1]:
            digits = []
            for digit2 in num2[::-1]:
                digit1 = int(digit1)
                digit2 = int(digit2)
                digits.append(digit1 * digit2 * mod)

            allDigits.append(int(self.carrySovler(digits)))
            mod *= 10

        return str(sum(allDigits))


num1 = "123"
num2 = "456"
slt = Solution()
print(slt.multiply(num1, num2))