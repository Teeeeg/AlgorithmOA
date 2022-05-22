def triplet_with_smaller_sum(arr, target):
    n = len(arr)
    if n < 3:
        return 0
    res = 0
    arr.sort()

    for i in range(n-2):
        l = i+1
        r = n-1
        if i > 0 and arr[i-1] == arr[i]:
            i += 1

        while l < r:
            total = arr[i]+arr[l]+arr[r]
            if total < target:
                # r的值大于l的值，则l, r之间的值替换r的值都满足题意
                res += r-l
                l += 1
            else:
                r -= 1

    return res

# Time O(n2)
# Space O(n)


arr = [-1, 0, 2, 3]
target = 3
print(triplet_with_smaller_sum(arr, target))
