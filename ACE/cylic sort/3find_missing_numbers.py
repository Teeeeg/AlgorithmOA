def find_missing_numbers(nums):
    n = len(nums)
    res = []
    i = 0

    while i < n:
        j = nums[i]-1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    # 返回的应该是i+1，应该在的数字
    for i in range(n):
        if nums[i] != i+1:
            res.append(i+1)

    return res


# Time O(n)
# Space o(1)

nums = [2, 3, 1, 8, 2, 3, 5, 1]
print(find_missing_numbers(nums))
