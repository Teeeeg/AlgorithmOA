class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1.0 / self.myPowCore(x, -n)
        else:
            return self.myPowCore(x, n)

    def myPowCore(self, x, n):
        if n == 0:
            return 1

        res = self.myPowCore(x, n//2)
        if n % 2:
            return res * res * x
        else:
            return res * res


x = 2.00000
n = 10
solution = Solution()
print(solution.myPow(x, n))
