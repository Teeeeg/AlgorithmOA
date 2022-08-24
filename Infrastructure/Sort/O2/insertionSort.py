def insertionSort(nums):
    n = len(nums)

    for i in range(n):
        # 被判断的数
        num = nums[i]
        # 表示前一个下标
        j = i-1
        # 往前比较，一直找到比标记位小的位置
        while j >= 0 and num < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        # 应该插入第一个比他小的后面
        nums[j+1] = num

    return nums


nums = [3, 2, 1, 5, 4]
print(insertionSort(nums))
