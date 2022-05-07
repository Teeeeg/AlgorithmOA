from random import randint


# 选择pivot点
def getPivotIndex(left, right):
    return randint(left, right)


def partition(nums, left, right):
    index = getPivotIndex(left, right)
    pivot = nums[index]
    # 将pivot 放到最后去
    nums[index], nums[right] = nums[right], nums[index]
    # i用来表示比pivot小的下标
    i = left

    # 遍历，将比pivot小的与i位置的进行交换
    for j in range(left, right):
        if nums[j] <= pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    # 最后将pivot放回去
    # 最终i就是pivot应该在的地方
    nums[i], nums[right] = nums[right], nums[i]
    # 返回基准点所在元素的正确索引
    return i

# 双边循环


def partition1(nums, left, right):
    pivotVal = nums[left]
    i, j = left, right
    while i < j:
        # 先从最右边找到一个比它小的
        while i < j and nums[j] > pivotVal:
            j -= 1
        # 找比他大的
        while i < j and nums[i] <= pivotVal:
            i += 1
        # 交换
        nums[i], nums[j] = nums[j], nums[i]
    # 归位
    nums[i], nums[left] = nums[left], nums[i]
    return i


def quickSort(nums, left, right):
    if left >= right:
        return

    pivotIndex = partition1(nums, left, right)
    quickSort(nums, left, pivotIndex-1)
    quickSort(nums, pivotIndex+1, right)


nums = [3, 2, 1, 5, 4]
# nums1 = [2, 3, 5, 7, 1, 6, 3, 3, 4, 7, 3, 2, 1]

# quickSort(nums1, 0, len(nums1)-1)
quickSort(nums, 0, len(nums)-1)
print(nums)
# print(nums1)
