def can_partition(nums, sum):
    n = len(nums)
    dp = [[False] * (sum+1) for _ in range(2)]

    for i in range(2):
        dp[i][0] = True

    for target in range(sum+1):
        dp[0][target] = nums[0] == target

    for i in range(1, n):
        for target in range(1, sum+1):
            dp[i % 2][target] = dp[(i-1) % 2][target]

            if nums[i] <= target:
                dp[i % 2][target] = dp[(
                    i-1) % 2][target] or dp[(i-1) % 2][target-nums[i]]

    return dp[(n-1) % 2][-1]


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
    print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))


main()
