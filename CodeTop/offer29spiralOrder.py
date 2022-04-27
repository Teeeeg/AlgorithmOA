from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix)
        res = []
        top, bot, left, right = 0, m-1, 0, n-1

        while top <= bot and left <= right:
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top += 1
            if top > bot:
                break

            for i in range(top, bot+1):
                res.append(matrix[right][i])
            right -= 1
            if left > right:
                break

            for i in range(right, left-1, -1):
                res.append(matrix[i][bot])
            bot -= 1
            if top > bot:
                break

            for i in range(bot, top-1, -1):
                res.append(matrix[left][i])
            left += 1
            if left > right-1:
                break

        return res


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
solution = Solution()
print(solution.spiralOrder(matrix))
