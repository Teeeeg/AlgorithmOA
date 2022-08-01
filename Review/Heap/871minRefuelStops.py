from heapq import heappop, heappush
from typing import List


class Solution:

    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        res = 0
        maxHeap = []
        remain = startFuel

        # pretend it if it can reach current station
        # add the target in the end
        for dist, fuel in stations + [[target, 0]]:
            # if it cannot actually reach
            # pop the max fuel to refuel to see if it can reach eventually
            while remain < dist:
                # if there is no fuel left, it means no
                if not maxHeap:
                    return -1
                remain -= heappop(maxHeap)
                res += 1
            heappush(maxHeap, -fuel)

        return res
