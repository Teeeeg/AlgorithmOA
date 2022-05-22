def remove_duplicates(arr):
    n = len(arr)

    if n == 1:
        return 1

    tail = 0
    next = 0

    while next < n:
        if arr[tail] != arr[next]:
            arr[tail+1], arr[next] = arr[next], arr[tail+1]
            tail += 1
        next += 1

    return tail+1


arr = [2, 3, 3, 3, 6, 9, 9]
print(remove_duplicates(arr))
