from typing import List


class Solution:
    '''
    Time: O(n)
    Space: O(n)

        x -------- y 
        1/ |1      1/1| \1 
    x1  x2      y1 y2 y3
        2/|2            2|\2
        x4 x5            y4 y5 
    
    # N = 11, count[x]  = 5, count[y] = 6 
    # ans[x] = x@x + y@y + count[y] = 6 + 7 + 6 = 19
    # ans[y] = y@y + x@x + count[x] = 7 + 6 + 5 = 18
    # ans[x] - ans[y] = count[y] - count[x]
    # ans[x] = ans[y] +  count[y] - count[x]
    # ans[x] = ans[y] + (N-count[x]) - count[x]
    '''

    def getGraph(self, n, edges):
        graph = {i: set() for i in range(n)}
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        return graph

    def updateCountandDist(self, graph, cur, parent, count, dist):
        for nbr in graph[cur]:
            if nbr == parent:
                continue

            self.updateCountandDist(graph, nbr, cur, count, dist)
            count[cur] += count[nbr]
            dist[cur] += dist[nbr] + count[nbr]

    def sumOfDistancesInTreeCore(self, graph, cur, parent, count, dist, n):
        for nbr in graph[cur]:
            if nbr == parent:
                continue

            dist[nbr] = dist[cur] + (n - count[nbr]) - count[nbr]
            self.sumOfDistancesInTreeCore(graph, nbr, cur, count, dist, n)

    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = self.getGraph(n, edges)
        count = [1] * n
        dist = [0] * n
        self.updateCountandDist(graph, 0, -1, count, dist)
        self.sumOfDistancesInTreeCore(graph, 0, -1, count, dist, n)

        return dist


n = 6
edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
slt = Solution()
print(slt.sumOfDistancesInTree(n, edges))
