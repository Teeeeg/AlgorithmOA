from collections import defaultdict
from typing import List


class Solution:
    # brute permutate

    def buildGraph(self, roads: List[List[int]]):
        graph = defaultdict(list)

        for a, b, cost in roads:
            graph[a].append((b, cost))

        return graph

    def minCostCore(self, n, graph, city, visited, cost, res):
        if len(visited) == n:
            res['minCost'] = min(res['minCost'], cost)

        for nextCity, nextCost in graph[city]:
            if nextCity in visited:
                continue

            visited.add(nextCity)
            self.minCostCore(n, graph, nextCity, visited, cost + nextCost, res)
            visited.remove(nextCity)

    def minCost(self, n: int, roads: List[List[int]]):
        if n == 0 or not roads or not roads[0]:
            return 0

        visited = set([1])
        res = {'minCost': (2 << 31) - 1}

        graph = self.buildGraph(roads)
        self.minCostCore(n, graph, 1, visited, 0, res)

        return res['minCost']


class Solution1:
    # use prunning

    def buildGraph(self, n, roads: List[List[int]]):
        MAX = (2 << 31) - 1
        graph = {i: {j: MAX for j in range(1, n + 1)} for i in range(1, n + 1)}

        for a, b, cost in roads:
            graph[a][b] = min(graph[a][b], cost)
            graph[b][a] = min(graph[b][a], cost)

        return graph

    def minCostCore(self, n, graph, city, visited, cost, path, res):
        if len(visited) == n:
            res['minCost'] = min(res['minCost'], cost)

        for nextCity in graph[city]:
            if nextCity in visited:
                continue

            if not self.hasBetterPath(graph, path, nextCity):
                continue

            visited.add(nextCity)
            path.append(nextCity)
            self.minCostCore(n, graph, nextCity, visited, cost + graph[city][nextCity], path, res)
            path.pop()
            visited.remove(nextCity)

    # determine if this path will lead to better one
    def hasBetterPath(self, graph, path, city):
        for i in range(1, len(path)):
            # in each swap, if it has a better path, it return False
            # this path won't lead to optimal
            if graph[path[i - 1]][path[i]] + graph[path[-1]][city] > graph[path[i - 1]][path[-1]] + graph[path[i][city]]:
                return False
        return True

    def minCost(self, n: int, roads: List[List[int]]):
        if n == 0 or not roads or not roads[0]:
            return 0

        visited = set([1])
        res = {'minCost': (2 << 31) - 1}

        graph = self.buildGraph(n, roads)
        self.minCostCore(n, graph, 1, visited, 0, [], res)

        return res['minCost']


class Solution2:

    def buildGraph(self, n, roads):
        MAX = (2 << 31) - 1
        graph = {i: {j: MAX for j in range(1, n + 1)} for i in range(1, n + 1)}

        for a, b, cost in roads:
            graph[a][b] = min(graph[a][b], cost)
            graph[b][a] = min(graph[b][a], cost)

        return graph

    def minCost(self, n: int, roads: List[List[int]]):
        MAX = (2 << 31) - 1
        # number of 2^n state
        stateSize = (1 << n)

        # opt[stateId][j] means the min cost at stateId and end with city j
        opt = [[MAX] * (n + 1) for _ in range(stateSize)]
        opt[1][1] = 0
        graph = self.buildGraph(n, roads)

        for state in range(stateSize):
            for i in range(2, n + 1):
                # current city
                if state & (1 << (i - 1)) == 0:
                    continue
                preState = state ^ (1 << (i - 1))
                # previous city
                for j in range(1, n + 1):
                    if preState & (1 << (j - 1)) == 0:
                        continue
                    opt[state][i] = min(opt[state][i], opt[preState][j] + graph[j][i])

        return min(opt[stateSize - 1])


n = 3
roads = [[1, 2, 1], [2, 3, 2], [1, 3, 3]]
slt = Solution2()
print(slt.minCost(n, roads))