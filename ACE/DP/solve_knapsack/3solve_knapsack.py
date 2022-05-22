# 自底向上
def solve_knapsack(profits, weights, capacity):
    n = len(profits)
    dp = [[0]*(capacity+1) for _ in range(n)]

    for cap in range(capacity+1):
        if weights[0] <= cap:
            dp[0][cap] = profits[0]

    for i in range(1, n):
        for cap in range(1, capacity+1):
            if weights[i] > cap:
                dp[i][cap] = dp[i-1][cap]
            else:
                dp[i][cap] = max(dp[i-1][cap], profits[i] +
                                 dp[i-1][cap-weights[i]])

    return dp[-1][-1]

# Time (nc)    n*c 个可能
# Space (c)    

def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()
