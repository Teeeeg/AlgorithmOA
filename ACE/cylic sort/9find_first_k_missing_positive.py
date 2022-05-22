def find_first_k_missing_positive(nums, k):
    n = len(nums)
    i = 0
    count = k
    res = []

    while i < n:
        j = nums[i]-1
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    # for i in range(n):
    #     if nums[i] != i+1 and count > 0:
    #         res.append(i+1)
    #         count -= 1

    # last = max(nums)+1
    # while count > 0:
    #     res.append(last)
    #     last += 1
    #     count -= 1

    extra = []
    for i in range(n):
        if nums[i] != i+1 and count > 0:
            res.append(i+1)
            extra.append(nums[i])
            count -= 1

    i = 1
    while count > 0:
        candidate = n+i
        if candidate not in extra:
            res.append(candidate)
            count -= 1
        i += 1

    return res


nums = [3, -1, 4, 5, 5]
k = 3
print(find_first_k_missing_positive(nums, k))
