from typing import List

n = int(input())
data = [time for time in input().split(' ')]


def solveData(data: List[str]):
    res = []
    for time in data:
        hour, minute, second = time.split(":")
        offset = int(second) + int(minute) * 60 + int(hour) * 60 * 60
        res.append((offset, time))
    return res


def solve():
    DAY = 60 * 60 * 24
    offsetTimes = solveData(data)
    n = len(offsetTimes)
    offsetTimes.sort(key=lambda x: x[0])
    diffs = []
    for i in range(1, n):
        diffs.append((offsetTimes[i][0] - offsetTimes[i - 1][0], offsetTimes[i - 1][1]))
    diffs.append((offsetTimes[0][0] - offsetTimes[-1][0] + DAY, offsetTimes[-1][1]))

    maxDiff = max(diffs, key=lambda x: x[0])
    print(maxDiff[1])


solve()