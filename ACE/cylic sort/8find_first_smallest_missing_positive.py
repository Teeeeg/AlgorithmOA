def find_first_smallest_missing_positive(nums):
    n = len(nums)
    i = 0
    res = n+1

    while i < n:
        # 利用范围排序
        j = nums[i]-1
        # 忽略不在这个范围内的值
        if nums[i] <= n and nums[i] > 0 and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    # 第一个不满足条件的值便是答案
    for i in range(n):
        if nums[i] != i+1:
            res = i+1
            break

    return res


# Time O(n)
# Space o(1)
nums = [3, -2, 0, 1, 2]
print(find_first_smallest_missing_positive(nums))
