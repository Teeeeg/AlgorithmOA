from typing import List


def can_attend_all_appointments(intervals: List):
    n = len(intervals)
    if n < 2:
        return True

    intervals.sort(key=lambda x: x[0])

    start = intervals[0][0]
    end = intervals[0][1]

    for i in range(1, n):
        interval = intervals[i]
        # 重叠了，则一定会一个的开始介于另一个的开始和结束之间
        # 有重叠, start <= cur.start <= end
        if start < interval[0] and interval[0] < end:
            return False
        start = interval[0]
        end = interval[1]

    return True

# Time O(nlogn) for sorting


def main():
    print("Can attend all appointments: " +
          str(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]])))
    print("Can attend all appointments: " +
          str(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]])))
    print("Can attend all appointments: " +
          str(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]])))


main()
