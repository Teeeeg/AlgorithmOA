class Fib:

    def fibCore(self, x):
        if self.cache[x]:
            return self.cache[x]

        if x == 0:
            return 0

        if x == 1:
            return 1

        self.cache[x] = self.fibCore(x - 1) + self.fibCore(x - 2)
        return self.cache[x]

    def fib(self, n):
        self.cache = [0] * (n + 1)
        self.cache[0] = 0
        self.cache[1] = 1

        return self.fibCore(n)

    def fibDynamic(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1

        opt = [0] * (n + 1)
        opt[1] = 1

        for i in range(2, n + 1):
            opt[i] = opt[i - 2] + opt[i - 1]

        return opt[-1]


fib = Fib()
print(fib.fibDynamic(9))