from typing import List


class Solution:

    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # proof
        # swwap proof
        # S is initial after p, q
        #
        # do p first max(max(p.minimal, S + p.actual) + q.actual, q.minimal)
        # do q first max(max(q.minimal, S + q.actual) + p.actual, p.minimal)
        tasks.sort(key=lambda x: x[0] - x[1])
        res = 0
        # assume 0 at the end
        # rewind to sums up
        for task in tasks[::-1]:
            res = max(task[1], res + task[0])

        return res