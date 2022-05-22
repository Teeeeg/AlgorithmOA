def remove_element(arr, key):
    n = len(arr)
    slot = 0
    next = 0

    while next < n:
        if arr[next] != key:
            arr[slot] = arr[next]
            slot += 1
        next += 1

    return slot


arr = [3, 2, 3, 6, 3, 10, 9, 3]
Key = 3
print(remove_element(arr, Key))
