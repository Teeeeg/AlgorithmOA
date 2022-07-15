def checkColinear(a, b, c):
    if a.x == b.x:
        return c.x == a.x
    if c.x == a.x:
        return a.x == b.x
    return (a.y - b.y) / (a.x - b.x) == (c.y - a.y) / (c.x - a.x)


def solution(A):
    n = len(A)
    res = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if checkColinear(A[i], A[j], A[k]):
                    res += 1

    return res
