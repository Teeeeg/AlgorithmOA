from typing import List


def binarySearch(nums: List[int], target: int):
    left = 0
    right = len(nums) - 1

    while left + 1 < right:
        mid = (left + right) // 2

        if nums[mid] < target:
            left = mid
        elif nums[mid] == target:
            right = mid
        else:
            right = mid

    # left is first position
    if nums[left] == target:
        return left

    if nums[right] == target:
        return right

    return -1


nums = [1, 1, 1, 1, 2]
print(binarySearch(nums, 3))