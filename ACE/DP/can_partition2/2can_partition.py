def can_partition(nums, sum):
    n = len(nums)
    dp = [[-1] * (sum+1) for _ in range(n)]
    return recursiveCore(nums, sum, 0, dp)


def recursiveCore(nums, target, index, dp):
    if target == 0:
        return True

    if index >= len(nums):
        return False

    if dp[index][target] != -1:
        return dp[index][target]

    res1 = False
    if nums[index] <= target:
        res1 = recursiveCore(nums, target-nums[index], index+1, dp)
    res2 = recursiveCore(nums, target, index+1, dp)

    dp[index][target] = res1 or res2
    return res1 or res2


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
    print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))


main()
