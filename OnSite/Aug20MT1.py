from typing import List

n = int(input())
data = [input() for _ in range(2)]


def solve(data: List[str], size):
    n = size
    res = []

    for i in range(n):
        res.append(data[0][i])
        res.append(data[1][i])

    return ''.join(res)


print(solve(data, n))