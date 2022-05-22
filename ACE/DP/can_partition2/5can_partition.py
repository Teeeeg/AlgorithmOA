def can_partition(nums, sum):
    n = len(nums)
    dp = [False] * (sum+1)

    dp[0] = True

    for target in range(sum+1):
        dp[target] = nums[0] == target

    for i in range(1, n):
        for target in range(sum, 0, -1):
            dp[target] = dp[target]

            if nums[i] <= target:
                dp[target] = dp[target] or dp[target-nums[i]]

    return dp[-1]


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
    print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))


main()
