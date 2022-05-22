def can_partition(nums):
    total = sum(nums)
    n = len(nums)
    dp = [False] * (total//2+1)

    dp[0] = True

    for target in range(total // 2+1):
        dp[target] = nums[0] == target

    for i in range(1, n):
        for target in range(total//2, -1, -1):
            dp[target] = dp[target]

            if nums[i] <= target:
                dp[target] = dp[target] or dp[target-nums[i]]

    opt = 0
    for i in range(total//2, -1, -1):
        if dp[i]:
            opt = i
            break

    return total-2*opt


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 9])))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
    print("Can partition: " + str(can_partition([1, 3, 100, 4])))


main()
