from typing import List

n = int(input())
data = [int(x) for x in input().split()]


def solve(data: List[int], n):
    oddMax = 0
    oddTotal = 0
    evenMax = 0
    evenTotal = 0
    res = 0

    for i in range(n):
        if data[i] % 2:
            oddMax = max(oddMax, data[i])
            oddTotal += data[i]

        else:
            evenMax = max(evenMax, data[i])
            evenTotal += data[1]

    for i in range(n):
        if data[i] % 2:
            if data[i] != oddMax:
                res += 1
        else:
            if data[i] != evenMax:
                res += 1

    if evenTotal == oddTotal:
        res += n // 2

    return res


res = solve(data, n)
print(res)
