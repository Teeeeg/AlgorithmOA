def search_bitonic_array(arr, key):
    n = len(arr)
    peakIndex = findPeak(arr)

    leftRes = binarySearch(arr, key, 0, peakIndex)
    rightRes = binarySearch(arr, key, peakIndex, n-1)

    if leftRes == -1 and rightRes == -1:
        return -1

    return leftRes if leftRes != -1 else rightRes


def binarySearch(arr, key, start, end):
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] == key:
            return mid
        if arr[mid] < key:
            start = mid+1
        else:
            end = mid-1

    return -1


def findPeak(arr):
    n = len(arr)
    start, end = 0, n-1

    while start < end:
        mid = (start+end) // 2
        if arr[mid] < arr[mid+1]:
            start = mid+1
        else:
            end = mid

    return start


def main():
    print(search_bitonic_array([1, 3, 8, 4, 3], 4))
    print(search_bitonic_array([3, 8, 3, 1], 8))
    print(search_bitonic_array([1, 3, 8, 12], 12))
    print(search_bitonic_array([10, 9, 8], 10))


main()
