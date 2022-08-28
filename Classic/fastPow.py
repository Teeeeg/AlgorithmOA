class Solution:

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            return 1 / self.myPow(x, -n)

        y = self.myPow(x, n // 2)

        if n % 2 == 0:
            return y * y
        else:
            return y * y * x
