from collections import defaultdict
from heapq import heappop, heappush


class Solution:

    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        graph = defaultdict(list)
        inDegrees = [0] * (n + 1)
        res = [0] * (n + 1)
        value = 1

        for i in range(n):
            if pattern[i] == 'I':
                graph[i].append(i + 1)
                inDegrees[i + 1] += 1
            else:
                graph[i + 1].append(i)
                inDegrees[i] += 1

        minHeap = []
        for i in range(n + 1):
            if inDegrees[i] == 0:
                minHeap.append(i)

        while minHeap:
            cur = heappop(minHeap)
            res[cur] = value
            value += 1
            if cur in graph:
                for child in graph[cur]:
                    inDegrees[child] -= 1
                    if inDegrees[child] == 0:
                        heappush(minHeap, child)

        res = [str(x) for x in res]
        return ''.join(res)


pattern = 'IIIDIDDD'
slt = Solution()
print(slt.smallestNumber(pattern))