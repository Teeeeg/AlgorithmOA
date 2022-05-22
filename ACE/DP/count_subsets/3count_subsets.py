def count_subsets(nums, target):
    n = len(nums)
    dp = [[0] * (target+1) for _ in range(n)]

    for target in range(target+1):
        dp[0][target] = 1 if nums[0] == target else 0

    for i in range(n):
        dp[i][0] = 1

    for i in range(1, n):
        for t in range(1, target+1):
            dp[i][t] += dp[i-1][t]
            if nums[i] < t:
                dp[i][t] += dp[i-1][t] + dp[i-1][t-nums[i]]

    return dp[-1][-1]


def main():
    print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


main()
