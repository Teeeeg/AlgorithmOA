from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals or not intervals[0]:
            return True
        intervals.sort(key=lambda x: x[0])
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            if end > intervals[i][0]:
                return False
            end = intervals[i][1]

        return True


intervals = [[0, 30], [5, 10], [15, 20]]
intervals1 = [[7, 10], [2, 4]]
solution = Solution()
print(solution.canAttendMeetings(intervals1))
