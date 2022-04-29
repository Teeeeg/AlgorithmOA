def mergeSort(nums):
    n = len(nums)
    # base case 1个的时候
    if n <= 1:
        return

    mid = n // 2
    left = nums[:mid]
    right = nums[mid:]

    # 递归调用
    mergeSort(left)
    mergeSort(right)

    # 递归处理逻辑
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1


nums = [3, 2, 1, 5, 4]
mergeSort(nums)
print(nums)
