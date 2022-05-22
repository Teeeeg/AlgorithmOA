from __future__ import print_function


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def merge(intervals: Interval):
    if len(intervals) < 2:
        return intervals

    # 排序之后保证 a.start <= b.start
    intervals.sort(key=lambda x: x.start)
    start = intervals[0].start
    end = intervals[0].end
    res = []

    for i in range(1, len(intervals)):
        cur = intervals[i]
        # 有重叠, start <= cur.start <= end
        if cur.start <= end:
            end = max(end, cur.end)
        else:
            res.append(Interval(start, end))
            start = cur.start
            end = cur.end

    res.append(Interval(start, end))
    return res


def main():
    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval()
    print()


main()
