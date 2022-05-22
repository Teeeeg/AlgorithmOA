def cyclic_sort(nums):
    n = len(nums)
    i = 0

    # 利用条件交换

    while i < n:
        # 该数字应该在的位置
        j = nums[i]-1
        # 交换
        if nums[i] != nums[j]:
            nums[j], nums[i] = nums[i], nums[j]
        else:
            i += 1

    return nums


# Time O(n)
# Space O(1)
