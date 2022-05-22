from collections import deque


def find_subarrays(arr, target):
    n = len(arr)
    win_start = 0
    win_prod = 1
    res = []

    # 目标是扩展到最大的窗口
    for win_end in range(n):
        win_prod *= arr[win_end]
        # 找到满足条件的最大区间
        while win_start < win_end and win_prod >= target:
            win_prod /= arr[win_start]
            win_start += 1
        tmp = deque()
        # 因为l,r之间的和都小于目标值，则内部都满足，用队列保证顺序
        for i in range(win_end, win_start-1, -1):
            tmp.appendleft(arr[i])
            res.append(list(tmp))

    return res

# Time O(n3)
# Space O(n)


arr = [2, 5, 3, 10]
target = 30
print(find_subarrays(arr, target))
