def can_partition(nums, sum):
    return recursiveCore(nums, sum, 0)


def recursiveCore(nums, target, index):
    if target == 0:
        return True

    if index >= len(nums):
        return False

    res1 = False
    if nums[index] <= target:
        res1 = recursiveCore(nums, target-nums[index], index+1)
    res2 = recursiveCore(nums, target, index+1)

    return res1 or res2


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
    print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))


main()
