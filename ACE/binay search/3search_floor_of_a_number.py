def search_floor_of_a_number(arr, key):
    n = len(arr)
    l, r = 0, n-1
    if key < arr[0]:
        return -1

    while l <= r:
        mid = (l+r) // 2
        if arr[mid] == key:
            return mid
        if arr[mid] < key:
            l = mid+1
        else:
            # 保证最后的arr[r] < key
            r = mid-1

    return r


def main():
    print(search_floor_of_a_number([4, 6, 10], 6))
    print(search_floor_of_a_number([1, 3, 8, 10, 15], 12))
    print(search_floor_of_a_number([4, 6, 10], 17))
    print(search_floor_of_a_number([4, 6, 10], -1))


main()
