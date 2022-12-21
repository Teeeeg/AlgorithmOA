from collections import deque
from typing import List


class Solution:

    def canVisitAllRoomsCore(self, rooms: List[List[int]], source):
        n = len(rooms)
        visited = [0] * n
        queue = deque()
        queue.append(source)
        visited[source] = 1

        count = 0

        while queue:
            cur = queue.popleft()
            count += 1

            if count == n:
                return True

            for child in rooms[cur]:
                if visited[child]:
                    continue

                visited[child] = 1
                queue.append(child)

        return False

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if self.canVisitAllRoomsCore(rooms, 0):
            return True

        return False


rooms = [[1], [], [0, 3], [1]]
slt = Solution()
print(slt.canVisitAllRooms(rooms))