def can_partition(nums):
    total = sum(nums)
    n = len(nums)
    if total % 2 == 1:
        return False

    dp = [[False] * (total // 2 + 1) for _ in range(2)]

    # 初始化，target=0时，不添加即可达成
    for i in range(2):
        dp[i][0] = True

    # 初始化，target == nums[0] 成立
    for target in range(total // 2):
        dp[0][target] = nums[0] == target

    for i in range(n):
        for target in range(total//2 + 1):
            dp[i % 2][target] = dp[(i-1) % 2][target]
            if nums[i] <= target:
                dp[i % 2][target] = dp[(
                    i-1) % 2][target] or dp[(i-1) % 2][target-nums[i]]

    return dp[(n-1) % 2][-1]


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()
