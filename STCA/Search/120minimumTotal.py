from typing import List


class Solution:

    def minimumTotalCore(self, triangle: List[List[int]], x, y, path, res):
        if x == len(triangle):
            res['min'] = min(res['min'], path)
            return

        self.minimumTotalCore(triangle, x + 1, y, path + triangle[x][y], res)
        self.minimumTotalCore(triangle, x + 1, y + 1, path + triangle[x][y], res)

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        res = {'min': (2 << 31) - 1}
        self.minimumTotalCore(triangle, 0, 0, 0, res)
        return res['min']


class Solution1:

    def minimumTotalCore(self, triangle: List[List[int]], memo: List[List[int]], x, y):
        if x == len(triangle):
            return 0

        if memo[x][y] != -1:
            return memo[x][y]

        leftRes = self.minimumTotalCore(triangle, memo, x + 1, y)
        rightRes = self.minimumTotalCore(triangle, memo, x + 1, y + 1)
        memo[x][y] = min(leftRes, rightRes) + triangle[x][y]

        return memo[x][y]

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        memo = [[-1] * m for _ in range(m)]

        return self.minimumTotalCore(triangle, memo, 0, 0)