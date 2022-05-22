from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        if not image or not image[0]:
            return [[]]

        lenCol = len(image[0])

        for row in image:
            row.reverse()
            for i in range(lenCol):
                row[i] ^= 1

        return image


image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
solution = Solution()
print(solution.flipAndInvertImage(image))
