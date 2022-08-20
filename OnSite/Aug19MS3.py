from collections import defaultdict


class Solution:

    def buildGraph(self, A, B):
        self.graph = [[-1] * (self.n + 1) for _ in range(self.n + 1)]
        for i in range(self.n):
            x = A[i]
            y = B[i]
            self.graph[x][y] = 1
            self.graph[y][x] = 1

    def minCostCore(self, x):
        childrend = []
        for y in range(self.n + 1):
            if self.graph[x][y] != -1 and y not in self.visited:
                childrend.append(y)

        if len(childrend) == 0:
            return (1, 1)

        totalPeople = 0
        for child in childrend:
            self.visited.add(child)
            res = self.minCostCore(child)
            fuel = res[0]
            people = res[1]
            self.totalFuel += fuel
            totalPeople += people

        newPeople = totalPeople + 1
        fuelRequired = 0
        if newPeople // 5 == 0:
            fuelRequired = 1
        else:
            if newPeople % 5:
                fuelRequired = (newPeople // 5) + 1
            else:
                fuelRequired = newPeople // 5

        return fuelRequired, newPeople

    def minCost(self, A, B):
        self.n = len(A)
        self.buildGraph(A, B)
        self.totalFuel = 0
        self.visited = set([0])
        self.minCostCore(0)
        return self.totalFuel


def solution(A, B):
    slt = Solution()
    return slt.minCost(A, B)


A = [0, 0, 0, 1, 1, 1, 9, 9, 9]
B = [7, 8, 1, 2, 3, 9, 4, 5, 6]
print(solution(A, B))