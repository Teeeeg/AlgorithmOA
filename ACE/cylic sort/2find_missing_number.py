def find_missing_number(nums):
    n = len(nums)
    i = 0

    while i < n:
        j = nums[i]
        # 舍弃最后一个数字，因为n-1
        if nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i:
            return i

    return n

# Time O(n)
# Space o(1)


nums = [7, 3, 5, 2, 4, 6, 0, 1]
print(find_missing_number(nums))
