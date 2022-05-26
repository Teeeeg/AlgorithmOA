def find_target_subsets(nums, target):
    n = len(nums)
    total = sum(nums)
    m = (total+target)//2
    dp = [[0] * (m+1) for _ in range(2)]

    for t in range(m):
        dp[0][t] = 1 if nums[0] == t else 0

    for i in range(2):
        dp[i][0] = 1

    for i in range(1, n):
        for j in range(1, m+1):
            dp[i % 2][j] = dp[(i-1) % 2][j]
            if nums[i] <= j:
                dp[i % 2][j] = dp[(i-1) % 2][j] + dp[(i-1) % 2][j-nums[i]]

    return dp[(m-1) % 2][-1]


def main():
    print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
    print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))


main()