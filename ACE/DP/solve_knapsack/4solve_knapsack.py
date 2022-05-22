# 减少空间为2c
def solve_knapsack(profits, weights, capacity):
    n = len(profits)
    dp = [[0]*(capacity+1) for _ in range(2)]

    for cap in range(capacity+1):
        if weights[0] <= cap:
            dp[0][cap] = profits[0]

    for i in range(1, n):
        for cap in range(1, capacity+1):
            dp[i % 2][cap] = dp[(i-1) % 2][cap]

            if weights[i] <= cap:
                dp[i % 2][cap] = max(dp[(i-1) % 2][cap], profits[i] +
                                     dp[(i-1) % 2][cap-weights[i]])

    return dp[(n-1) % 2][-1]

# Time (nc)    n*c 个可能
# Space (c)


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()
