from heapq import heappop, heappush


def find_closest_elements(arr, K, X):
    n = len(arr)
    # 利用二分缩小范围
    pivot = binarySearch(arr, X)
    maxHeap = []

    left, right = pivot-K, pivot+K
    left = max(left, 0)
    right = min(right, n)

    for i in range(left, right):
        if len(maxHeap) < K:
            heappush(maxHeap, (-abs(arr[i]-X), arr[i]))
        else:
            if -abs(arr[i]-X) > maxHeap[0][0]:
                heappop(maxHeap)
                heappush(maxHeap, (-abs(arr[i]-X), arr[i]))

    return [_[1] for _ in maxHeap]


def binarySearch(arr, target):
    n = len(arr)
    left, right = 0, n-1

    while left <= right:
        mid = (left+right) // 2
        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            left = mid+1
        else:
            right = mid-1

    return left

# Time O(NlogN + KlogK)


def main():
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))


main()
