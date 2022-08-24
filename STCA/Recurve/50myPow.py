class Solution:

    def myPow(self, x: float, n: int) -> float:
        # base
        if n == 0:
            return 1
        # chech if n is negative
        if n < 0:
            return 1 / (self.myPow(x, -n))

        # record the n//2
        y = self.myPow(x, n // 2)
        # if n is even
        if n % 2 == 0:
            return y * y
        else:
            # is odd
            return y * y * x


x = 2.00000
n = -2147483648
slt = Solution()
print(slt.myPow(x, n))
