from typing import List


class Solution:

    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        if not startTime:
            return 0

        n = len(startTime)
        res = 0

        for i in range(n):
            interval = (startTime[i], endTime[i])
            if interval[0] <= queryTime <= interval[1]:
                res += 1

        return res