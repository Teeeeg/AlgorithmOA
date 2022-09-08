class Solution:

    def countOnes(self, num: int):
        res = 0
        while num:
            if num % 10 == 1:
                res += 1
            num //= 10

        return res

    def countDigitOne(self, n: int) -> int:
        res = 0

        for num in range(1, n + 1):
            res += self.countOnes(num)

        return res


slt = Solution()
print(slt.countDigitOne(13))