def can_partition(nums):
    total = sum(nums)
    n = len(nums)
    dp = [[False] * (total//2+1) for _ in range(n)]

    for i in range(n):
        dp[i][0] = True

    for target in range(total // 2+1):
        dp[0][target] = nums[0] == target

    for i in range(1, n):
        for target in range(1, total//2+1):
            if nums[i] <= target:
                dp[i][target] = dp[i-1][target] or dp[i-1][target-nums[i]]
            else:
                dp[i][target] = dp[i-1][target]

    opt = 0
    for i in range(total//2, -1, -1):
        flag = False
        for j in range(n):
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
