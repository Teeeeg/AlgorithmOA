# O(n2)
# Think of it this way: a bubble passes over the list, ‘catches’ the maximum/minimum element, and brings it over to the right side.
def bubbleSort(nums):
    n = len(nums)

    for i in range(n):
        # 最后一个元素已归位
        for j in range(n - i - 1):
            # 将大的和向后面的交换
            # 比下一个元素大则与它交换
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums


# 倒着来的


def bubbleSort1(nums):
    n = len(nums)

    for i in range(n - 1, -1, -1):
        for j in range(n - 1, n - 1 - i, -1):
            if nums[j - 1] > nums[j]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]

    return nums


nums = [3, 2, 1, 5, 4]
print(bubbleSort(nums))

nums1 = [2, 3, 5, 7, 1, 6, 3, 3, 4, 7, 3, 2, 1]
print(bubbleSort1(nums1))
