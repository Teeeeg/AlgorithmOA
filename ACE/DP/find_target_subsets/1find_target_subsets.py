def find_target_subsets(nums, target):
    res = recursiveCore(nums, target, 0, 0)
    return res


def recursiveCore(nums, target, index, total):
    if index == len(nums) and total == target:
        return 1

    if len(nums) <= index:
        return 0

    res1 = recursiveCore(nums, target, index+1, total+nums[index])
    res2 = recursiveCore(nums, target, index+1, total-nums[index])

    return res1 + res2


def main():
    print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
    print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))


main()
