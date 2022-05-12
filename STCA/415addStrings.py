class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        n1 = len(num1)
        n2 = len(num2)
        i = n1-1
        j = n2-1
        carry = 0

        while i >= 0 or j >= 0:
            digit1 = num1[i] if i >= 0 else '0'
            digit2 = num2[j] if j >= 0 else '0'
            total = int(digit1) + int(digit2) + carry
            carry = total//10
            res.append(str(total % 10))

            i -= 1
            j -= 1

        if carry:
            res.append(str(carry))

        return ''.join(reversed(res))


num1 = "456"
num2 = "77"
soltuion = Solution()
print(soltuion.addStrings(num1, num2))
