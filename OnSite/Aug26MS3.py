def solution(A, B):
    MAX = 10**9
    n = len(A)
    minExcluded = MAX

    for i in range(n):
        if A[i] == B[i]:
            continue

        curExcluded = A[i] if A[i] < B[i] else B[i]
        minExcluded = min(curExcluded, minExcluded)

    return minExcluded if minExcluded != MAX else A[-1] + 1