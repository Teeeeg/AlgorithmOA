def binary_search(arr, key):
    n = len(arr)
    l, r = 0, n-1
    ascending = arr[l] <= arr[r]

    while l <= r:
        mid = (l+r) // 2
        if arr[mid] == key:
            return mid

        if ascending:
            if arr[mid] > key:
                r = mid-1
            else:
                l = mid+1
        else:
            if arr[mid] > key:
                l = mid+1
            else:
                r = mid-1
    return -1


def main():
    print(binary_search([4, 6, 10], 10))
    print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
    print(binary_search([10, 6, 4], 10))
    print(binary_search([10, 6, 4], 4))


main()
