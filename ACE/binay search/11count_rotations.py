# 在无序区间找
def count_rotations(arr):
    n = len(arr)
    start, end = 0, n-1

    while start <= end:
        mid = (start+end) // 2
        # 分别去前后比较
        # 寻找最小值
        if arr[mid] < arr[mid-1]:
            return mid
        if arr[mid+1] < arr[mid]:
            return mid+1

        # 去找寻找非排序区间
        if arr[start] < arr[mid]:
            start = mid+1
        else:
            end = mid-1

    return 0


def main():
    print(count_rotations([10, 15, 1, 3, 8]))
    print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
    print(count_rotations([1, 3, 8, 10]))


main()
