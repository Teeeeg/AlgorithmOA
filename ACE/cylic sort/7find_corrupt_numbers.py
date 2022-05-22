def find_corrupt_numbers(nums):
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
            res = [nums[i], i+1]

    return res


# Time O(n)
# Space o(1)
nums = [3, 1, 2, 3, 6, 4]
print(find_corrupt_numbers(nums))
