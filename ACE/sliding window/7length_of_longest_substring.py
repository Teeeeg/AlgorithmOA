def length_of_longest_substring(arr, k):
    n = len(arr)
    win_start = 0
    count = 0
    res = 0

    for win_end in range(n):
        right_num = arr[win_end]
        if arr[right_num] == 0:
            count += 1

        win_len = win_end - win_start + 1

        if win_len - count > k:
            if arr[win_start] == 1:
                count -= 1
            win_start += 1

        res = max(res, win_end-win_start+1)

    return res


Array = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
k = 2
print(length_of_longest_substring(Array, 2))
