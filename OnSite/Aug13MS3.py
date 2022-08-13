def solution(A, X, Y):
    n = len(A)
    dist = (X - 1) * Y

    res = (2 << 31) - 1

    for left in range(0, n - dist):
        right = left
        total = 0
        count = 0
        while count < X:
            total += A[right]
            right += Y
            count += 1
        res = min(res, total)

    return res


def solutionCore(A, X, Y, index, curCost, count, memo):
    minCost = 2**31 - 1
    if (index, count) in memo:
        return memo[(index, count)]

    if index >= len(A) and count == 0:
        return curCost

    if index >= len(A):
        return minCost

    if count == 0:
        return curCost

    curr = solutionCore(A, X, Y, index + Y, A[index] + curCost, count - 1, memo)
    skipCur = solutionCore(A, X, Y, index + 1, 0, X, memo)
    minCost = min(minCost, curr, skipCur)
    memo[(index, count)] = minCost
    return minCost


def solution1(A, X, Y):
    memo = {}
    ans = solutionCore(A, X, Y, 0, 0, X, memo)
    return ans


class Solution:

    def sovleCore(self, index, count, path):
        MAX = (1 << 31) - 1
        minCost = MAX

        if (index, count) in self.opt:
            return self.opt[(index, count)]

        if count == 0:
            return path

        if index >= self.n:
            return minCost

        cur = self.sovleCore(index + self.Y, count - 1, path + self.A[index])
        skipCur = self.sovleCore(index + 1, self.X, 0)

        minCost = min(minCost, cur, skipCur)
        self.opt[(index, count)] = minCost

        return minCost

    def sovle(self, A, X, Y):
        self.A = A
        self.n = len(A)
        self.X = X
        self.Y = Y
        self.opt = {}

        res = self.sovleCore(0, X, 0)
        return res


A = [4, 2, 3, 7]
A1 = [10, 3, 4, 7]
A2 = [4, 2, 5, 4, 3, 5, 1, 4, 2, 7]

print(solution1(A, 2, 2))
print(solution1(A1, 2, 3))
print(solution1(A2, 3, 2))

print('+++++++++++++++')
slt = Solution()
print(slt.sovle(A, 2, 2))
print(slt.sovle(A1, 2, 3))
print(slt.sovle(A2, 3, 2))