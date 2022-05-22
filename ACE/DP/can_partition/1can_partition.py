def can_partition(nums):
    total = sum(nums)
    if total % 2 == 1:
        return False

    return recursiveCore(nums, 0, total//2)


def recursiveCore(nums, index, target):
    if target == 0:
        return True

    if index >= len(nums):
        return False

    res1 = False

    if nums[index] <= target:
        res1 = recursiveCore(nums, index+1, target-nums[index])

    res2 = recursiveCore(nums, index+1, target)

    return res1 or res2


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()
