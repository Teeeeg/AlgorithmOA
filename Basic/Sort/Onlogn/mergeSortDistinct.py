from typing import List


def appendDistinct(tmp, nums, index):
    if not (tmp and tmp[-1] == nums[index]):
        tmp.append(nums[index])


def mergeTwoDistinct(nums: List[int], nums1: List[int]):
    tmp = []
    l = 0
    r = 0

    while l < len(nums) and r < len(nums1):
        if nums[l] <= nums1[r]:
            appendDistinct(tmp, nums, l)
            l += 1
        else:
            appendDistinct(tmp, nums1, r)
            r += 1

    while l < len(nums):
        appendDistinct(tmp, nums, l)
        l += 1

    while r < len(nums1):
        appendDistinct(tmp, nums1, r)
        r += 1

    return tmp


def mergeSortCore(nums: List[int]):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    leftRes = mergeSortCore(nums[:mid])
    rightRes = mergeSortCore(nums[mid:])
    res = mergeTwoDistinct(leftRes, rightRes)
    return res


def mergeSort(nums: List[int]):
    if not nums:
        return

    return mergeSortCore(nums)


nums = [1, 4, 5, 6, 3, 1, 10]
print(mergeSort(nums))
