def find_target_subsets(nums, target):
    n = len(nums)
    m = sum(nums)
    dp = [[False]*(m) for _ in range(n)]
    res = recursiveCore(nums, target, 0, 0, dp)
    return res


def recursiveCore(nums, target, index, total, dp):
    if index == len(nums) and total == target:
        return 1

    if len(nums) <= index:
        return 0

    if dp[index][total]:
        return dp[index][total]

    res1 = recursiveCore(nums, target, index+1, total+nums[index], dp)
    res2 = recursiveCore(nums, target, index+1, total-nums[index], dp)

    dp[index][total] = res1 + res2
    return res1 + res2


def main():
    print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
    print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))


main()
