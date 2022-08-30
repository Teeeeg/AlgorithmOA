from collections import deque
from heapq import heappop, heappush
from typing import List


class Solution:

    def buildGraph(self, times: List[List[int]], n: int):
        graph = {i: [] for i in range(1, n + 1)}

        for time in times:
            src = time[0]
            dest = time[1]
            delay = time[2]
            graph[src].append((dest, delay))

        return graph

    # SPFA
    # basic idea is
    # if path of a node get shorter, add it back for further updates
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = self.buildGraph(times, n)
        dist = {i: 10**9 for i in range(1, n + 1)}
        dist[k] = 0
        minHeap = [(0, k)]

        while minHeap:
            curDelay, cur = heappop(minHeap)
            for neighbor, delay in graph[cur]:
                nextDelay = curDelay + delay
                if nextDelay >= dist[neighbor]:
                    continue
                # if it nextDelay is shorter
                # update it and add it for further update
                dist[neighbor] = nextDelay
                heappush(minHeap, (nextDelay, neighbor))

        res = max(dist.values())
        return res if res != 10**9 else -1


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
slt = Solution()
print(slt.networkDelayTime(times, n, k))
