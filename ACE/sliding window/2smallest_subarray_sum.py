def smallest_subarray_sum(s, arr):
    n = len(arr)
    win_start = 0
    win_sum = 0
    res = n+1

    for win_end in range(n):
        win_sum += arr[win_end]
        while win_sum >= s:
            res = min(res, win_end-win_start+1)
            win_sum -= arr[win_start]
            win_start += 1

    return 0 if res == n+1 else res


arr = [2, 1, 5, 2, 3, 2]
S = 7
print(smallest_subarray_sum(S, arr))
