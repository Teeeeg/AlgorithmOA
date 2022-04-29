def mySort(nums):
    n = len(nums)
    if n <= 1:
        return

    mid = n // 2
    left = nums[: mid]
    right = nums[mid:]
    mySort(left)
    mySort(right)

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
print(mySort(nums))
print(nums)
