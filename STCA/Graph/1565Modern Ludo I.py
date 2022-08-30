from collections import deque
from typing import (
    List,)


class Solution:
    # SPFA
    def buildGraph(self, length: int, connections: List[List[int]]):
        graph = {i: set() for i in range(1, length + 1)}

        for connection in connections:
            src = connection[0]
            dest = connection[1]
            graph[src].add(dest)

        return graph

    def modern_ludo(self, length: int, connections: List[List[int]]) -> int:
        graph = self.buildGraph(length, connections)
        dist = {1: 0}
        queue = deque([1])

        while queue:
            # roll the dice  dist + 1
            cur = queue.popleft()
            for step in range(1, 7):
                neighbor = cur + step
                if neighbor > length:
                    break
                if neighbor in dist and dist[neighbor] <= dist[cur] + 1:
                    continue
                dist[neighbor] = dist[cur] + 1
                queue.append(neighbor)

            # direct pass  dist + 0
            for neighbor in graph[cur]:
                if neighbor in dist and dist[neighbor] <= dist[cur]:
                    continue
                dist[neighbor] = dist[cur]
                queue.append(neighbor)

        return dist[length] if length in dist else -1


length = 695
connections = [[554, 695], [495, 609], [6, 31], [462, 597], [140, 611], [431, 686], [270, 473], [80, 131], [235, 422], [15, 278], [264, 363], [289, 407], [12, 130], [432, 660], [183, 285], [340, 583],
               [282, 405], [139, 206], [189, 412], [338, 404], [97, 200], [21, 353], [95, 208], [370, 614], [89, 217], [171, 317], [47, 581], [192, 560], [177, 264], [173, 395], [228, 636],
               [168, 223], [414, 419], [160, 236], [54, 326], [474, 639], [471, 525], [101, 393], [149, 213], [460, 568], [527, 632], [383, 409], [283, 310]]
slt = Solution()
print(slt.modern_ludo(length, connections))