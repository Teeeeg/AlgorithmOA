def find_target_subsets(nums, target):
    n = len(nums)
    total = sum(nums)
    m = (total+target)//2
    dp = [0] * (m+1)

    for t in range(m+1):
        dp[t] = 1 if nums[0] == t else 0

    dp[0] = 1

    for i in range(1, n):
        for j in range(m, 0, -1):
            if nums[i] <= j:
                dp[j] += dp[j-nums[i]]

    return dp[-1]


def main():
    print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
    print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))


main()
