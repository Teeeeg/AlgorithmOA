import math


def find_max_in_bitonic_array(arr):
    n = len(arr)
    start, end = 0, n-1

    # start == end指到一起，为最大值
    while start < end:
        # 向下取整
        mid = (start+end) // 2
        if arr[mid] < arr[mid+1]:
            start = mid+1
        else:
            end = mid
    return arr[start]


def main():
    print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
    print(find_max_in_bitonic_array([3, 8, 3, 1]))
    print(find_max_in_bitonic_array([1, 3, 8, 12]))
    print(find_max_in_bitonic_array([10, 9, 8]))


main()
