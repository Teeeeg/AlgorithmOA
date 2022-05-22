def merge(intervals_a, intervals_b):
    na = len(intervals_a)
    nb = len(intervals_b)
    i, j = 0, 0
    res = []

    while i < na and j < nb:
        # 重叠了，则一定会一个的开始介于另一个的开始和结束之间
        aOverb = intervals_a[i][0] <= intervals_b[j][1] and intervals_a[i][0] >= intervals_b[j][0]
        bOvera = intervals_b[j][0] <= intervals_a[i][1] and intervals_b[j][0] >= intervals_a[i][0]

        if aOverb or bOvera:
            start = max(intervals_a[i][0], intervals_b[j][0])
            end = min(intervals_a[i][1], intervals_b[j][1])
            res.append([start, end])

        if intervals_a[i][1] < intervals_b[j][1]:
            i += 1
        else:
            j += 1

    return res

# Time O(n+m)


def main():
    print("Intervals Intersection: " +
          str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
    print("Intervals Intersection: " +
          str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


main()
