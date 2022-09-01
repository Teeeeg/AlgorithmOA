from math import sqrt


def getCompleteFactors(n):
    factors = [1, n]
    sqrtOfN = sqrt(n)
    factor = 2

    while factor <= sqrtOfN:
        if n % factor == 0:
            factors.append(factor)
            n //= factor
            sqrtOfN = sqrt(n)
        else:
            factor += 1

    factors.append(n)

    return factors


print(getCompleteFactors(12))
