from typing import List


class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)
        n = len(matrix[0])

        index = [0, n - 1]

        while index[0] < m and index[1] >= 0:
            if matrix[index[0]][index[1]] == target:
                return True

            if target > matrix[index[0]][index[1]]:
                index[0] += 1
            else:
                index[1] -= 1

        return False