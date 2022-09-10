class Solution:

    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)

        flag = 1 if numerator * denominator < 0 else 0

        n = abs(numerator)
        d = abs(denominator)

        res = []
        if flag:
            res.append('-')

        res.append(str(n // d))
        res.append('.')
        n %= d
        visited = {}

        while n:
            n *= 10

            if n in visited:
                index = visited[n]
                res.insert(index, '(')
                res.append(')')
                break

            digit = n // d
            res.append(str(digit))
            visited[n] = len(res) - 1
            n %= d

        return ''.join(res)


numerator = 22
denominator = 7
slt = Solution()
print(slt.fractionToDecimal(numerator, denominator))