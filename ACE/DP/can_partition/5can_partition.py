def can_partition(nums):
    total = sum(nums)
    n = len(nums)
    if total % 2 == 1:
        return False

    dp = [False] * (total // 2 + 1)

    # 初始化，target=0时，不添加即可达成
    dp[0] = True

    # 初始化，target == nums[0] 成立
    for target in range(total // 2):
        dp[target] = nums[0] == target

    for i in range(1, n):
        for target in range(total//2, 0, -1):
            dp[target] = dp[target]

            if nums[i] <= target:
                dp[target] = dp[target] or dp[target-nums[i]]

    return dp[-1]


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()
