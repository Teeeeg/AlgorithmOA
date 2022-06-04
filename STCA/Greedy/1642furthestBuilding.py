from heapq import heappop, heappush
from typing import List


class Solution:
    # 贪心
    # 先用砖头
    # 没砖头的时候再用梯子
    # 在用过最大砖头的地方用梯子

    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        maxHeap = []
        res = 0

        for i in range(1, n):
            diff = heights[i] - heights[i - 1]
            if diff <= 0:
                res += 1
                continue

            heappush(maxHeap, -diff)
            bricks -= diff

            if bricks >= 0:
                res += 1
            elif bricks < 0 and ladders:
                ladders -= 1
                bricks -= heappop(maxHeap)
                res += 1
            else:
                break

        return res


heights = [4, 12, 2, 7, 3, 18, 20, 3, 19]
bricks = 10
ladders = 2
slt = Solution()
print(slt.furthestBuilding(heights, bricks, ladders))
