from heapq import heappop, heappush
from typing import List


class Solution:

    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Sort tasks by start time
        sortedTasks = sorted([(start, task_length, index) for index, (start, task_length) in enumerate(tasks)], reverse=True)
        ans = []
        curTime = 0
        minHeap = []

        while sortedTasks or minHeap:
            # No more queued sortedTasks; jump ahead to next arrival
            if not minHeap:
                curTime = max(curTime, sortedTasks[-1][0])

            # Add all sortedTasks that have arrived by the current time
            while sortedTasks and sortedTasks[-1][0] <= curTime:
                start, process_time, task_index = sortedTasks.pop()
                # Heap is ordered by process time and old task index
                heappush(minHeap, (process_time, task_index))

            nextTaskLength, nextTaskIndex = heappop(minHeap)
            ans.append(nextTaskIndex)

            # Advance time forward
            curTime += nextTaskLength

        return ans


tasks = [[1, 2], [2, 4], [3, 2], [4, 1]]
slt = Solution()
print(slt.getOrder(tasks))