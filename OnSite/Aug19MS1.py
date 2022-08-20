from typing import List


def solution(X: List[int], Y: List[int], W: int):
    n = len(X)
    X.sort()
    res = 0
    i = 0

    while i < n:
        cover = X[i] + W
        while i < n and X[i] <= cover:
            i += 1
        res += 1

    return res


X = [2, 4, 2, 6, 7, 1]
Y = [0, 5, 3, 2, 1, 5]
W = 2
print(solution(X, Y, W))