def find_range(arr, key):
    res = [-1, -1]
    res[0] = find_index(arr, key, False)
    if res[0] != -1:
        res[1] = find_index(arr, key, True)
    return res


def find_index(arr, key, findMax):
    keyIndex = -1
    n = len(arr)
    start, end = 0, n-1
    while start <= end:
        mid = (start+end) // 2

        # 找到对应的值后，扩大搜索边界
        if arr[mid] == key:
            keyIndex = mid
            if findMax:
                # 要寻找有边界，则在mid，end上找
                start = mid+1
                # 要寻找有边界，则在start，mid上找
            else:
                end = mid-1

        if arr[mid] < key:
            start = mid+1
        elif arr[mid] > key:
            end = mid-1
    return keyIndex


def main():
    print(find_range([4, 6, 6, 6, 9], 6))
    print(find_range([1, 3, 8, 10, 15], 10))
    print(find_range([1, 3, 8, 10, 15], 12))


main()
