from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)
        n = len(matrix[0])

        row = 0
        col = n-1

        while row < m and col >= 0:
            node = matrix[row][col]
            if node == target:
                return True
            elif node < target:
                row += 1
            else:
                col -= 1

        return False


matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22],
          [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
target = 5
solution = Solution()
print(solution.findNumberIn2DArray(matrix, target))
