def shortest_window_sort(arr):
    n = len(arr)
    l, r = 0, n-1

    # 找到前后第一个不满足排序的数

    while l < r and arr[l+1] > arr[l]:
        l += 1
    while l < r and arr[r-1] < arr[r]:
        r -= 1

    # 处理特殊情况，相交说明他们本身就有序
    if l == r:
        return 0

    # 获取l，r之间的最小最大值
    maxOfSub = max(arr[l: r+1])
    minOfSub = min(arr[l: r+1])

    # 扩展范围
    # 因为第一个不按序的可能其前面有比他大的数
    for i in range(l):
        if arr[i] >= minOfSub:
            l = i
    # 因为第一个不按序的可能其后面有比他小的数
    for i in range(r+1, n):
        if arr[i] <= maxOfSub:
            r = i

    # [1, 3, 2, 0, -1, 7, 10]
    # 找到不按序的后，把中间的排序
    # [1, -1, 0, 2, 3, 7, 10]
    # 则需要上述的扩展

    return r-l+1

# Time O(n)


arr = [1, 2, 3]
print(shortest_window_sort(arr))
