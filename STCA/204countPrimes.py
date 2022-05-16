class Solution:

    def countPrimes(self, n: int) -> int:
        res = 0
        for x in range(2, n):
            if self.isPrime(x):
                res += 1

        return res

    def isPrime(self, x):
        for y in range(2, x):
            if x % y == 0:
                return False

        return True


class Solution1:

    def countPrimes(self, n: int) -> int:
        res = 0
        primes = [1] * n
        for x in range(2, n):
            if primes[x]:
                res += 1
                for i in range(x * x, n, x):
                    primes[i] = 0

        return res


slt = Solution1()
print(slt.countPrimes(10))
