from random import randint


def getPivotIndex(left, right):
    return randint(left, right)


def partition(nums, left, right):
    pivotIndex = getPivotIndex(left, right)
    pivotVal = nums[pivotIndex]
    nums[pivotIndex], nums[right] = nums[right], nums[pivotIndex]
    smaller = left

    for i in range(left, right):
        if nums[i] <= pivotVal:
            nums[smaller], nums[i] = nums[i], nums[smaller]
            smaller += 1

    nums[right], nums[smaller] = nums[smaller], nums[right]

    return smaller


def quickSort(nums):
    n = len(nums)
    quickSortCore(nums, 0, n - 1)


def quickSortCore(nums, left, right):
    if left >= right:
        return

    pivotIndex = partition(nums, left, right)

    quickSortCore(nums, left, pivotIndex - 1)
    quickSortCore(nums, pivotIndex + 1, right)


nums = [3, 2, 1, 5, 4]
quickSort(nums)
print(nums)
# word = 'hello'
# print(sorted(word))
