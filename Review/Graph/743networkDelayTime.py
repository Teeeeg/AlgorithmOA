from heapq import heappop, heappush
import math
from typing import List


class Solution:

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        for time in times:
            if time[0] not in graph:
                graph[time[0]] = []
            graph[time[0]].append((time[1], time[2]))

        # dist records smallest value
        dist = [math.inf] * (n + 1)
        dist[k] = 0
        minQueue = [(0, k)]

        while minQueue:
            # get the smallest node
            curTime, curNode = heappop(minQueue)
            # if current smallest is bigger than record
            # cutting early
            if dist[curNode] < curTime:
                continue
            # update its neighbors
            if curNode in graph:
                for node, time in graph[curNode]:
                    # update nextTime with current dist
                    if (nextTime := time + curTime) < dist[node]:
                        dist[node] = nextTime
                        heappush(minQueue, (nextTime, node))

        res = max(dist[1:])
        return res if res != math.inf else -1  # type: ignore


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
slt = Solution()
print(slt.networkDelayTime(times, n, k))
