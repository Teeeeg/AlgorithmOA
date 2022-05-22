from __future__ import print_function
from heapq import heappop, heappush
import queue


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


class EmployeeInterval:

    def __init__(self, interval, employeeIndex, intervalIndex):
        self.interval = interval  # interval representing employee's working hours
        # index of the list containing working hours of this employee
        self.employeeIndex = employeeIndex
        self.intervalIndex = intervalIndex  # index of the interval in the employee list

    def __lt__(self, other):
        # min heap based on meeting.end
        return self.interval.start < other.interval.start


def find_employee_free_time(schedule):
    intervals = []
    res = []
    for individual in schedule:
        for interval in individual:
            intervals.append(interval)

    intervals.sort(key=lambda x: x.start)

    start = intervals[0].start
    end = intervals[0].end

    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval.start <= end:
            start = interval.start
            end = interval.end
        else:
            res.append(Interval(end, interval.start))

        start = interval.start
        end = interval.end
    return res

# Time O(n)
# Space O(1)


def find_employee_free_time(schedule):
    if not schedule:
        return []
    res = []
    miniHeap = []
    n = len(schedule)

    for i in range(n):
        heappush(miniHeap, EmployeeInterval(schedule[i][0], i, 0))

    preInterval = miniHeap[0].interval
    while miniHeap:
        queueTop = heappop(miniHeap)
        if queueTop.interval.start > preInterval.end:
            res.append(Interval(preInterval.end, queueTop.interval.start))
            preInterval = queueTop.interval
        else:
            if queueTop.interval.end > preInterval.end:
                preInterval = queueTop.interval

        nextSchedule = schedule[queueTop.employeeIndex]

        if queueTop.intervalIndex+1 < len(nextSchedule):
            heappush(miniHeap, EmployeeInterval(
                nextSchedule[queueTop.intervalIndex+1], queueTop.employeeIndex, queueTop.intervalIndex+1))

    return res


def main():

    input = [[Interval(1, 3), Interval(5, 6)], [
        Interval(2, 3), Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3), Interval(9, 12)], [
        Interval(2, 4)], [Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3)], [
        Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()


main()
