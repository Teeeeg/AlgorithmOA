n, m = [int(x) for x in input().split()]
probs = [int(x) for x in input().split()]
scores = [int(x) for x in input().split()]


class Solution:

    def solveCore(self, index, path, count):
        if index >= self.n:
            self.res = max(self.res, path / 100)
            return

        if count > 0:
            self.solveCore(index + 1, path + self.scores[index] * 100, count - 1)
        self.solveCore(index + 1, path + self.scores[index] * self.probs[index], count)

    def solve(self, n, m, probs, scores):
        if len(probs) != len(scores):
            return -1
        self.n = n
        self.probs = probs
        self.scores = scores
        self.res = 0

        self.solveCore(0, 0, m)

        return self.res


slt = Solution()
res = slt.solve(n, m, probs, scores)
print('%.2f' % res)

# def solve():
#     # opt[0][i] 第i道题不复习的最高分
#     # opt[1][i] 第i道题复习的最高分
#     opt = [[[0, 0]] * n for _ in range(2)]

#     opt[0][0] = [(probs[0] / 100) * scores[0], 0]
#     if m > 0:
#         opt[1][0] = [scores[0], 1]
#     res = 0

#     for i in range(1, n):
#         m1 = opt[0][i - 1][1]
#         m2 = opt[1][i - 1][1]

#         if opt[0][i][0] < opt[0][i - 1][0] + (probs[i] / 100) * scores[i]:
#             opt[0][i] = [opt[0][i - 1][0] + (probs[i] / 100) * scores[i], m1]
#         if opt[0][i][0] < opt[1][i - 1][0] + (probs[i] / 100) * scores[i]:
#             opt[0][i] = [opt[1][i - 1][0] + (probs[i] / 100) * scores[i], m2]

#         if m1 < m:
#             if opt[1][i][0] < opt[0][i - 1][0] + scores[i]:
#                 opt[1][i] = [opt[0][i - 1][0] + scores[i], m1 + 1]
#         if m2 < m:
#             if opt[1][i][0] < opt[1][i - 1][0] + scores[i]:
#                 opt[1][i] = [opt[1][i - 1][0] + scores[i], m2 + 1]

#         res = max(res, opt[0][i][0], opt[1][i][0])
#     return res
