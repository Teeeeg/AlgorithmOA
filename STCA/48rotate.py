from typing import List


class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        if not matrix and not matrix[0]:
            return
        n = len(matrix)

        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for line in matrix:
            line.reverse()


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
slt = Solution()
slt.rotate(matrix)
print(matrix)