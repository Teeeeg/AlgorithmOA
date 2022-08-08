# brute
def solve(x, y):
    n = len(x)
    res = 0

    for i in range(n):
        for j in range(n):
            if i != j:
                res = max(res, y[i] + y[j] + abs(x[i] - x[j]))

    return res


# reduce half the calculate by define j<i
def solve1(x, y):
    n = len(x)
    res = 0

    for i in range(1, n):
        for j in range(i):
            res = max(y[i] + x[i] + y[j] - x[j], res)

    return res


# reduce + opreator by introducing preMax to cache
# and seperate i and j
def solve2(x, y):
    n = len(x)
    MIN = -2**31 - 1
    res = 0

    for i in range(1, n):
        preMax = MIN
        for j in range(i):
            preMax = max(y[j] - x[j], preMax)
        res = max(preMax + y[i] + x[i], res)

    return res


# reduce to O(n)
# preMAX always check the max y[j] - x[j] before the i
# so cache every step
# each step update the preMax with only one y[j] - x[j]
# which comes to preMax is always the max y[j] - x[j] which j vary for 0 - i-1
def solve3(x, y):
    n = len(x)
    MIN = -2**31 - 1
    res = 0
    preMax = MIN

    for i in range(1, n):
        preMax = max(preMax, y[i - 1] - x[i - 1])
        res = max(preMax + y[i] + x[i], res)

    return res


x = [1, 2, 3]
y = [0, 3, 5]

print(solve(x, y))
print(solve1(x, y))
print(solve2(x, y))
print(solve3(x, y))
