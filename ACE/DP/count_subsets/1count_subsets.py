def count_subsets(nums, sum):
    return recursiveCore(nums, sum, 0)


def recursiveCore(nums, target, index):
    if target == 0:
        return 1
    if index >= len(nums):
        return 0

    res1 = 0
    if nums[index] <= target:
        res1 = recursiveCore(nums, target-nums[index], index+1)
    res2 = recursiveCore(nums, target, index+1)

    return res1+res2


def main():
    print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


main()
