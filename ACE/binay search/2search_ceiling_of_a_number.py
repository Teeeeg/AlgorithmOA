def search_ceiling_of_a_number(arr, key):
    n = len(arr)
    l, r = 0, n-1
    # base case
    # key > arr[-1]说明无解
    if key > arr[n-1]:
        return -1

    while l <= r:
        mid = (l+r) // 2
        # 若找到，则返回该值
        if arr[mid] == key:
            return mid
        if arr[mid] > key:
            r = mid-1
        # 保证最后的arr[l] > key
        else:
            l = mid+1

    return l


def main():
    print(search_ceiling_of_a_number([4, 6, 10], 6))
    print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
    print(search_ceiling_of_a_number([4, 6, 10], 17))
    print(search_ceiling_of_a_number([4, 6, 10], -1))


main()
