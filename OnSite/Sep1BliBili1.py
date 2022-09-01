from math import sqrt

n = int(input())


def solve(n):
    total = 0
    div = 2
    sqrtOfN = sqrt(n)

    while div <= sqrtOfN:
        if n % div == 0:
            total += div
            n //= div
            sqrtOfN = sqrt(n)
        else:
            div += 1

    return total + n


print(solve(n))
