from heapq import heappop, heappush
import math
from typing import List


class Solution:
    # Dijsktra
    # Greedy approach
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        for time in times:
            if time[0] not in graph:
                graph[time[0]] = []
            graph[time[0]].append((time[1], time[2]))

        # dist records smallest value
        dist = [math.inf] * (n + 1)
        visited = [False] * (n + 1)
        self.path = [-1] * (n + 1)
        self.longestPath = []
        dist[k] = 0
        minQueue = [(0, k)]

        while minQueue:
            # get the smallest node
            curTime, curNode = heappop(minQueue)
            # update its neighbors
            if not visited[curNode]:
                visited[curNode] = True
                if curNode in graph:
                    for node, time in graph[curNode]:
                        # update nextTime with current dist
                        if (nextTime := time + curTime) < dist[node]:
                            dist[node] = nextTime
                            heappush(minQueue, (nextTime, node))
                            self.path[node] = curNode

        resIndex = -1
        res = -1
        for i in range(1, n + 1):
            if dist[i] > res:
                resIndex = i
                res = dist[i]

        self.getLongestPath(resIndex)
        print(self.longestPath)

        return res if res != math.inf else -1  # type: ignore

    def getLongestPath(self, index):
        if index == -1:
            return

        self.getLongestPath(self.path[index])
        self.longestPath.append(index)


class Solution1:
    # Bellman-Ford
    # if dist[y] > z + dist[x] than update
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        MAX = 2**31 - 1
        dist = [MAX] * (n + 1)
        self.path = [-1] * (n + 1)
        self.longestPath = []

        dist[k] = 0

        for _ in range(n - 1):
            updated = False
            for edge in times:
                x = edge[0]
                y = edge[1]
                z = edge[2]
                if dist[y] > z + dist[x]:
                    dist[y] = z + dist[x]
                    self.path[y] = x
                    updated = True
            # if during this iteration there is no update
            if not updated:
                break
        resIndex = -1
        res = -1
        for i in range(1, n + 1):
            if dist[i] > resIndex:
                resIndex = i
                res = dist[i]

        self.getLongestPath(resIndex)
        print(self.longestPath)

        return res if res != MAX else -1

    def getLongestPath(self, index):
        if index == -1:
            return

        self.getLongestPath(self.path[index])
        self.longestPath.append(index)


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
slt = Solution()
print(slt.networkDelayTime(times, n, k))
