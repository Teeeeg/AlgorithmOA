def can_partition(nums):
    total = sum(nums)
    n = len(nums)
    dp = [[False] * (total//2+1) for _ in range(2)]

    for i in range(2):
        dp[i][0] = True

    for target in range(total // 2+1):
        dp[0][target] = nums[0] == target

    for i in range(1, n):
        for target in range(1, total//2+1):
            dp[i % 2][target] = dp[(i-1) % 2][target]

            if nums[i] <= target:
                dp[i % 2][target] = dp[(
                    i-1) % 2][target] or dp[(i-1) % 2][target-nums[i]]

    opt = 0
    for i in range(total//2, -1, -1):
        flag = False
        for j in range(2):
            if dp[j][i]:
                opt = i
                flag = True
                break
        if flag:
            break

    return total-2*opt


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 9])))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
    print("Can partition: " + str(can_partition([1, 3, 100, 4])))


main()
