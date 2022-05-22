# 基于上一步发现
# dp[i % 2][cap] = max(dp[(i-1) % 2][cap], profits[i] + dp[(i-1) % 2][cap-weights[i]]
# 计算下一个数必须计算dp[c]和dp[c-weights[i]]
# 计算dp[c-weights[i]] 会出现问题，则考虑倒序
def solve_knapsack(profits, weights, capacity):
    n = len(profits)
    dp = [0]*(capacity+1)

    for cap in range(capacity+1):
        if weights[0] <= cap:
            dp[cap] = profits[0]

    for i in range(1, n):
        for cap in range(capacity, 0, -1):
            dp[cap] = dp[cap]

            if weights[i] <= cap:
                dp[cap] = max(dp[cap], profits[i] + dp[cap-weights[i]])

    return dp[-1]


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()
