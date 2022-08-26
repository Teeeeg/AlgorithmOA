# print("this is a debug message")

from collections import defaultdict
from typing import List


def solution(A, M):
    if not A:
        return 0

    n = len(A)

    res = 0

    for i in range(n):
        count = 0
        for j in range(n):
            diff = abs(A[i] - A[j])

            if diff % M == 0:
                count += 1

        res = max(count, res)

    return res


def solution1(A: List[int], M: int) -> int:
    dct = {}
    res = 0

    for num in A:
        modRes = num % M
        dct[modRes] = dct.get(modRes, 0) + 1

        if dct[modRes] > res:
            res = dct[modRes]

    return res