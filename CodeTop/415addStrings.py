class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        n1 = len(num1)
        n2 = len(num2)
        res = ''

        i1 = i2 = 0
        carry = 0
        while i1 < n1 or i2 < n2:
            digit1 = int(num1[i1]) if i1 < n1 else 0
            digit2 = int(num2[i2]) if i2 < n2 else 0
            total = digit1 + digit2 + carry
            carry = total // 10
            digit = total % 10
            res += str(digit)

            i1 += 1
            i2 += 1

        if carry:
            res += '1'

        return res[::-1]


num1 = "11"
num2 = "123"
solution = Solution()
print(solution.addStrings(num1, num2))
