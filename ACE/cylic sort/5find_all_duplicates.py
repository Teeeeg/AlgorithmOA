def find_all_duplicates(nums):
    n = len(nums)
    i = 0
    res = []

    while i < n:
        j = nums[i]-1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i+1:
            res.append(nums[i])

    return res


# Time O(n)
# Space o(1)
nums = [5, 4, 7, 2, 3, 5, 3]
print(find_all_duplicates(nums))
