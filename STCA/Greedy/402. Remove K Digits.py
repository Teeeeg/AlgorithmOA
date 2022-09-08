class Solution:

    def removeKdigits(self, num: str, k: int) -> str:
        monoStack = []

        for digit in num:
            while monoStack and monoStack[-1] > digit and k > 0:
                monoStack.pop()
                k -= 1

            monoStack.append(digit)

        res = ''
        while k > 0:
            monoStack.pop()
            k -= 1

        res = ''.join(monoStack).lstrip('0')

        return res if res else '0'


num = "112"
k = 1
slt = Solution()
print(slt.removeKdigits(num, k))