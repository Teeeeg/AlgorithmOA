# 双指针，0移动到left之前，2移动到right之后
# 1就自然而然到中间了
def dutch_flag_sort(arr):
    n = len(arr)
    l, r = 0, n-1

    i = 0
    while i <= r:
        if arr[i] == 0:
            arr[i], arr[l] = arr[l], arr[i]
            # i需要+1，因为前半部分0增多了
            # 且不是0的已经被处理掉了
            i += 1
            l += 1
        elif arr[i] == 1:
            i += 1
        else:
            # i不能+1，因为交换后可能为0，1，2
            arr[i], arr[r] = arr[r], arr[i]
            r -= 1
    return arr

# Time O(n)


arr = [2, 2, 0, 1, 2, 0]
print(dutch_flag_sort(arr))
