def count_subsets(nums, target):
    n = len(nums)
    dp = [[-1] * (target+1) for _ in range(n)]
    res = recursiveCore(nums, target, 0, dp)
    return res


def recursiveCore(nums, target, index, dp):
    if target == 0:
        return 1
    if index >= len(nums):
        return 0

    if dp[index][target] != -1:
        return dp[index][target]

    res1 = 0
    if nums[index] <= target:
        res1 = recursiveCore(nums, target-nums[index], index+1, dp)
    res2 = recursiveCore(nums, target, index+1, dp)

    dp[index][target] = res1+res2
    return res1+res2


def main():
    # print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


main()
