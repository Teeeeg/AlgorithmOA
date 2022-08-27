def solutionCore(S, start, end):
    if end - start + 1 < 2:
        return 0

    counter = [0] * 26
    for i in range(start, end + 1):
        index = ord(S[i]) - ord('a')
        counter[index] += 1

    for i in range(start, end + 1):
        index = ord(S[i]) - ord('a')

        if counter[index] % 2:
            return max(solutionCore(S, start, i - 1), solutionCore(S, i + 1, end))

    return end - start + 1


def solution(S: str):
    n = len(S)

    if n <= 1:
        return 0

    return solutionCore(S, 0, n - 1)


S = 'zthzthzzzz'
print(solution(S))
