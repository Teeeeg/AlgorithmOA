from typing import List


class Solution:
    # 深度优先
    def canVisitAllRoomsCore(self, rooms: List[List[int]], visited: List[bool], index):
        if visited[index]:
            return

        visited[index] = True
        for room in rooms[index]:
            self.canVisitAllRoomsCore(rooms, visited, room)

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n

        self.canVisitAllRoomsCore(rooms, visited, 0)
        # 返回是否全部访问过了
        return False if False in visited else True


rooms = [[1], [2], [3], []]
slt = Solution()
print(slt.canVisitAllRooms(rooms))