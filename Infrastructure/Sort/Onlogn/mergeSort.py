from typing import List


def mergeTwo(nums: List[int], left, mid, right):
    tmp = []
    l = left
    r = mid + 1

    while l <= mid and r <= right:
        if nums[l] <= nums[r]:
            tmp.append(nums[l])
            l += 1
        else:
            tmp.append(nums[r])
            r += 1

    while l <= mid:
        tmp.append(nums[l])
        l += 1

    while r <= right:
        tmp.append(nums[r])
        r += 1

    nums[left:right + 1] = tmp[:]


def mergeSortCore(nums: List[int], left, right):
    if left >= right:
        return

    mid = (left + right) >> 1
    mergeSortCore(nums, left, mid)
    mergeSortCore(nums, mid + 1, right)
    mergeTwo(nums, left, mid, right)


def mergeSort(nums: List[int]):
    if not nums:
        return
    n = len(nums)
    mergeSortCore(nums, 0, n - 1)


nums = [1, 3, 2, 3, 1]
mergeSort(nums)
print(nums)
