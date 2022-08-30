from typing import List


def append(tmp, nums, index):
    if not (tmp and tmp[-1] == nums[index]):
        tmp.append(nums[index])


def mergeTwoDistinct(nums: List[int], left, mid, right):
    tmp = []
    l = left
    r = mid + 1

    while l <= mid and r <= right:
        if nums[l] <= nums[r]:
            append(tmp, nums, l)
            l += 1
        else:
            append(tmp, nums, r)
            r += 1

    while l <= mid:
        append(tmp, nums, l)
        l += 1

    while r <= right:
        append(tmp, nums, r)
        r += 1

    return tmp