def make_squares(arr):
    n = len(arr)
    res = [0] * n
    l, r = 0, n-1
    slot = 0

    while l < r:
        sqrt_l = arr[l]*arr[l]
        sqrt_r = arr[r]*arr[r]
        if sqrt_l > sqrt_r:
            res[slot] = sqrt_l
            l += 1
        else:
            res[slot] = sqrt_r
            r -= 1
        slot += 1

    res.reverse()
    return res

# 优化不使用翻转
# 使用下表直接赋值


arr = [-2, -1, 0, 2, 3]
print(make_squares(arr))
