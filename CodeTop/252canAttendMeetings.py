from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        n = len(intervals)
        intervals.sort(key=lambda x: x[0])
        pre = None
        for interval in intervals:
            if not pre:
                pre = interval
                continue
            if pre[1] > interval[0]:
                return False
            pre = interval

        return True


intervals = [[0, 30], [60, 240], [90, 120]]
solution = Solution()
print(solution.canAttendMeetings(intervals))
