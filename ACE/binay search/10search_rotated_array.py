# 在有序区间找
def search_rotated_array(arr, key):
    n = len(arr)
    start, end = 0, n-1
    
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] == key:
            return mid

        # mid--end有序
        if arr[mid] <= arr[end]:
            # key在这个范围内
            if arr[mid] < key <= arr[end]:
                start = mid+1
            # 不在则在缩小范围
            else:
                end = mid-1
        else:
            if arr[start] <= key < arr[mid]:
                end = mid-1
            else:
                start = mid+1
    return -1


def main():
    print(search_rotated_array([10, 15, 1, 3, 8], 15))
    print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))


main()
