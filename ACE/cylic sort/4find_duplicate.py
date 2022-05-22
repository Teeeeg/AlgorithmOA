def find_duplicate(nums):
    n = len(nums)
    i = 0

    while i < n:
        # 入口为当前位置错位
        j = nums[i]-1
        if nums[i] != i+1:
            # 交换
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            # 如果相等，说明之前有，即重复
            else:
                return nums[i]
        else:
            i += 1

    return -1


# Time O(n)
# Space o(1)
nums = [2, 1, 3, 3, 5, 4]
print(find_duplicate(nums))
