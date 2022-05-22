def search_quadruplets(arr, target):
    n = len(arr)
    res = []
    arr.sort()

    for i in range(n-2):
        if arr[i] > target:
            break
        if i > 0 and arr[i] == arr[i-1]:
            i += 1

        for j in range(i+1, n-1):
            if arr[i]+arr[j] > target:
                break
            if j > i+1 and arr[j] == arr[j-1]:
                j += 1
            l, r = j+1, n-1

            while l < r:
                total = arr[i]+arr[j]+arr[l]+arr[r]
                if total == target:
                    res.append([arr[i], arr[j], arr[l], arr[r]])
                    l += 1
                    r -= 1
                    while l < r and arr[l] == arr[l-1]:
                        l += 1
                    while l < r and arr[r] == arr[r+1]:
                        r -= 1
                elif total < target:
                    l += 1
                else:
                    r -= 1

    return res


arr = [4, 1, 2, -1, 1, -3]
target = 1
print(search_quadruplets(arr, target))
