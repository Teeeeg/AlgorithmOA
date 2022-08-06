from typing import List


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.n = len(persons)
        self.voteCounts = {}
        self.tops = []

        for i in range(self.n):
            if persons[i] not in self.voteCounts:
                self.voteCounts[persons[i]] = 0
            self.voteCounts[persons[i]] += 1
            if not self.tops:
                self.tops.append((persons[i], times[i]))
            elif self.voteCounts[persons[i]] >= self.voteCounts[self.tops[-1][0]]:
                self.tops.append((persons[i], times[i]))
            else:
                self.tops.append((self.tops[-1][0], times[i]))

    def q(self, t: int) -> int:
        left = 0
        right = self.n - 1
        res = -1

        while left <= right:
            mid = (left + right) >> 1
            if self.tops[mid][1] > t:
                right = mid - 1
            else:
                left = mid + 1
                res = max(res, mid)

        return self.tops[res][0]


# ["TopVotedCandidate", "q", "q", "q", "q", "q", "q", "q", "q", "q", "q"]
# [[[0, 0, 0, 0, 1], [0, 6, 39, 52, 75]], [45], [49], [59], [68], [42], [37], [99], [26], [78], [43]]

persons = [0, 1, 1, 0, 0, 1, 0]
times = [0, 5, 10, 15, 20, 25, 30]
topVC = TopVotedCandidate(persons, times)
