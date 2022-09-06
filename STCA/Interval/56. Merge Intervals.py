from typing import List


class Solution:
    # consider a interval have effects in a [left, right]
    # prefix sum, prefix sum is zero means no effect

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        boundaries = []
        for interval in intervals:
            # -1 is start's flag
            # [1, 2(1)] [2(2), 3] need to merge, so 2(2) should be in the front
            boundaries.append((interval[0], -1))
            boundaries.append((interval[1], 1))

        boundaries.sort()
        overLapped = 0
        left = 0
        right = 0
        res = []

        for boundary in boundaries:
            if overLapped == 0:
                left = boundary[0]
            overLapped += boundary[1]

            if overLapped == 0:
                right = boundary[0]
                res.append([left, right])

        return res