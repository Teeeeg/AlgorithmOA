from typing import List

n, m, k = map(int, input().split())
roads = [[int(x) for x in input().split()] for _ in range(2)]
costs = [int(x) for x in input().split()]


class Solution:

class Solution:

    def buildGraph(self, roads: List[List[int]], costs: List[int]):
        graph = {}
        n = len(roads[0])

        for i in range(n):
            x = roads[0][i]
            y = roads[1][i]
            cost = costs[i]
            graph[x] = (y, cost)

        return graph

    def minCost(self, roads: List[List[int]], costs: List[int], k: int):
        graph = self.buildGraph(roads, costs)
        


slt = Solution()
print(slt.minCost(n, roads, costs, k))