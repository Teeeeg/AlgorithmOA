from collections import defaultdict
from typing import List


class Solution:

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegrees = [0] * numCourses
        graph = defaultdict(list)

        for p in prerequisites:
            inDegrees[p[0]] += 1
            graph[p[1]].append(p[0])

        queue = []
        for i in range(numCourses):
            if inDegrees[i] == 0:
                queue.append(i)

        res = []
        while queue:
            cur = queue.pop(0)
            res.append(cur)
            for post in graph[cur]:
                inDegrees[post] -= 1
                if inDegrees[post] == 0:
                    queue.append(post)

        return res if len(res) == numCourses else []


numCourses = 2
prerequisites = [[1, 0]]
slt = Solution()
print(slt.findOrder(numCourses, prerequisites))