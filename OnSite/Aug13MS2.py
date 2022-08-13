import math


def Solve(a, b):
    if not a or not b:
        return -1

    n = len(a)
    dct = {}
    res = 0
    MOD = 10**9 + 7

    for i in range(n):
        nume = a[i]
        deno = b[i]
        gcd = math.gcd(nume, deno)
        nume /= gcd
        deno /= gcd

        if (deno - nume, deno) in dct:
            res += dct[(deno - nume, deno)]
        dct[(nume, deno)] = dct.get((nume, deno), 0) + 1

    return res % MOD


X = [1, 1, 2]
Y = [3, 2, 3]
X1 = [1, 1, 1]
Y1 = [2, 2, 2]
X2 = [1, 2, 3, 1, 2, 12, 8, 4]
Y2 = [5, 10, 15, 2, 4, 15, 10, 5]

print(Solve(X, Y))
print(Solve(X1, Y1))
print(Solve(X2, Y2))