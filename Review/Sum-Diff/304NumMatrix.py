from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.sums = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                self.sums[i][j] = self.getSums(i - 1, j) + self.getSums(i, j - 1) - self.getSums(i - 1, j - 1) + matrix[i][j]

    def getSums(self, row, col):
        if row >= 0 and col >= 0:
            return self.sums[row][col]
        return 0

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.getSums(row2, col2) - self.getSums(row2, col1 - 1) - self.getSums(row1 - 1, col2) + self.getSums(row1 - 1, col1 - 1)


matrix = [[-1]]
slt = NumMatrix(matrix)
print(slt.sumRegion(0, 0, 0, 0))