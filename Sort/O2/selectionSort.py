# O(n2)
def selectionSort(nums):
    n = len(nums)

    # i指向已经排好序的最后一个
    for i in range(n):
        minIndex = i
        # 通过对比，找到未排序数组中最小的下标
        for j in range(i+1, n):
            minIndex = j if nums[minIndex] > nums[j] else minIndex
        # 交换数字
        nums[minIndex], nums[i] = nums[i], nums[minIndex]

    return nums


nums = [3, 2, 1, 5, 4]
print(selectionSort(nums))
