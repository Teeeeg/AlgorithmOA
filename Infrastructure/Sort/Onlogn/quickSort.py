from random import randint


# 选择pivot点
def getPivotIndex(left, right):
    return randint(left, right)


# 双边循环
def partition(nums, left, right):
    pivotIndex = randint(left, right)
    pivotVal = nums[pivotIndex]
    nums[left], nums[pivotIndex] = nums[pivotIndex], nums[left]
    l, r = left, right
    while l < r:
        # 必须先从最右边找到一个比它小的
        while l < r and nums[r] >= pivotVal:
            r -= 1
        # 找比他大的
        while l < r and nums[l] <= pivotVal:
            l += 1
        # 交换
        if l < r:
            nums[l], nums[r] = nums[r], nums[l]
    # 归位
    nums[l], nums[left] = nums[left], nums[l]
    return l


def quickSort(nums, left, right):
    if left >= right:
        return

    pivotIndex = partition(nums, left, right)
    quickSort(nums, left, pivotIndex - 1)
    quickSort(nums, pivotIndex + 1, right)


# nums = [3, 2, 1, 5, 4]
nums = [2, 3, 5, 7, 1, 6, 3, 3, 4, 7, 3, 2, 1]

# quickSort(nums1, 0, len(nums1)-1)
quickSort(nums, 0, len(nums) - 1)
print(nums)
# print(nums1)
