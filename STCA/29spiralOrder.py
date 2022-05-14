from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        m = len(matrix)
        n = len(matrix[0])
        res = []

        left = 0
        right = n-1
        top = 0
        bot = m-1

        while left <= right and top <= bot:
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top += 1
            if top > bot:
                break

            for i in range(top, bot+1):
                res.append(matrix[i][right])
            right -= 1
            if left > right:
                break

            for i in range(right, left-1, -1):
                res.append(matrix[bot][i])
            bot -= 1
            if top > bot:
                break

            for i in range(bot, top-1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right:
                break

        return res


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
solution = Solution()
print(solution.spiralOrder(matrix1))
