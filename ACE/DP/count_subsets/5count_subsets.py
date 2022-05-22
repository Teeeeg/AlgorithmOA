def count_subsets(nums, target):
    n = len(nums)
    dp = [0] * (target+1)

    for t in range(target):
        dp[t] = 1 if nums[0] == t else 0
    dp[0] = 1

    for i in range(1, n):
        for t in range(target, -1, -1):
            if nums[i] <= t:
                dp[t] += dp[t-nums[i]]

    return dp[-1]


def main():
    print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


main()
