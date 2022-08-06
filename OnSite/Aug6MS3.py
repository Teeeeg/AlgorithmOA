from collections import defaultdict


class Solution:

    def __init__(self, A, B, S) -> None:
        self.graph = defaultdict(list)
        self.A = A
        self.B = B
        self.S = S
        self.n = len(A)
        self.buildGraph()

    def buildGraph(self):
        for i in range(self.n):
            self.graph[i].append(self.A[i])
            self.graph[i].append(self.B[i])

    def bipartiteMatch(self, matchR, visited, patient):
        slots = self.graph[patient]
        for slot in slots:
            if not visited[slot]:
                visited[slot] = 1
                if matchR[slot] == -1 or self.bipartiteMatch(matchR, visited, matchR[slot]):
                    matchR[slot] = patient
                    return True
        return False

    def maxBPM(self):
        matchR = [-1] * (self.S + 1)
        res = 0
        for patient in range(self.n):
            visited = [0] * (self.S + 1)
            if self.bipartiteMatch(matchR, visited, patient):
                res += 1

        return res


def solution(A, B, S):
    if not A or not B or not S:
        return False

    if len(A) > S:
        return False

    slt = Solution(A, B, S)
    maxBPM = slt.maxBPM()
    return maxBPM == len(A)


A = [1, 1, 1, 3]
B = [3, 2, 2, 1]
S = 4
print(solution(A, B, S))