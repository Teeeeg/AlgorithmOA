def max_sub_array_of_size_k(k, arr):
    n = len(arr)
    win_start = 0
    win_sum = 0
    res = 0

    for win_end in range(n):
        win_sum += arr[win_end]
        while win_end-win_start+1 >= k:
            res = max(res, win_sum)
            win_sum -= arr[win_start]
            win_start += 1

    return res


arr = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sub_array_of_size_k(k, arr))
