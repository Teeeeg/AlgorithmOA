def search_triplets(arr):
    res = []
    n = len(arr)
    arr.sort()
    if n < 3:
        return res

    for i in range(n-2):
        if arr[i] >= 0:
            return res
        if i > 0 and arr[i] == arr[i-1]:
            i += 1

        l, r = i+1, n-1
        while l < r:
            triple = arr[i] + arr[l] + arr[r]
            if triple == 0:
                res.append([arr[i], arr[l], arr[r]])
                # 先跳过再更新
                r -= 1
                l += 1
                # 判段下一个迭代是否有重复
                while l <= r and arr[l] == arr[l-1]:
                    l += 1
                while l <= r and arr[r] == arr[r+1]:
                    r -= 1

            if triple < 0:
                l += 1
            else:
                r -= 1

    return res

# 排序O(nlogn)
# 双指针遍历整个列表O(n)
# 外层一个for
# 则最后时间复杂度综合为O(n2)

# 空间复杂度为O(n)主要用于排序


arr = [-5, 2, -1, -2, 3]
print(search_triplets(arr))
