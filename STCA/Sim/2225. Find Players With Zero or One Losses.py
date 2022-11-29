from typing import List


class Solution:

    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        p2count = {}

        for win, defeat in matches:
            p2count[win] = p2count.get(win, 0)

            p2count[defeat] = p2count.get(defeat, 0)
            p2count[defeat] += 1

        res0 = []
        res1 = []

        for p, count in p2count.items():
            if count == 1:
                res1.append(p)

            if count == 0:
                res0.append(p)

        res0.sort()
        res1.sort()

        return [res0, res1]
