def can_partition(nums):
    return recursiveCore(nums, 0, 0, 0)


def recursiveCore(nums, total1, total2, index):
    if len(nums) == index:
        return abs(total1-total2)

    res1 = recursiveCore(nums, total1+nums[index], total2, index+1)
    res2 = recursiveCore(nums, total1, total2+nums[index], index+1)

    return min(res1, res2)


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 9])))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
    print("Can partition: " + str(can_partition([1, 3, 100, 4])))


main()
