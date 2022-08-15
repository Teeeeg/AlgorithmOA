from typing import Counter

data = input()


def solve(data):
    if not data:
        return 0

    n = len(data)
    if n % 6:
        return -1
    counter = Counter(data)
    count = counter['f']

    for key, value in counter.items():
        if value != count:
            return -1
        if key not in 'failed':
            return -1

    indexOfF = []
    indexOfD = []
    for i in range(n):
        if data[i] == 'f':
            indexOfF.append(i)
        if data[i] == 'd':
            indexOfD.append(i)

    if len(indexOfD) != len(indexOfF):
        return -1

    intervals = []
    for i in range(len(indexOfF)):
        interval = (indexOfF[i], indexOfD[i])
        intervals.append(interval)

    intervals.sort(key=lambda x: x[0])

    res = 1
    merged = [intervals[0]]
    for i, interval in enumerate(intervals):
        if i == 0:
            continue
        if interval[0] <= merged[-1][1]:
            merged[-1] = (merged[-1][0], interval[1])
            res += 1
        else:
            merged.append(interval)

    return res


print(solve(data))