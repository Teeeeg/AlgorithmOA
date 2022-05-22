def insert(intervals, new_interval):
    n = len(intervals)
    res = []
    i = 0

    # 找到开始合并的index
    while i < n and intervals[i][1] < new_interval[0]:
        res.append(intervals[i])
        i += 1

    # 合并方法类似merge
    while i < n and new_interval[1] >= intervals[i][0]:
        # 更新new_interval
        new_interval[0] = min(intervals[i][0], new_interval[0])
        new_interval[1] = max(intervals[i][1], new_interval[1])
        i += 1

    res.append(new_interval)

    while i < n:
        res.append(intervals[i])
        i += 1

    return res


def main():
    print("Intervals after inserting the new interval: " +
          str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
    print("Intervals after inserting the new interval: " +
          str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
    print("Intervals after inserting the new interval: " +
          str(insert([[2, 3], [5, 7]], [1, 4])))


main()
