# 进一步优化，记忆已经计算过的
def solve_knapsack(profits, weights, capacity):
    # 记忆
    dp = [[-1] * (capacity+1) for _ in range(len(profits))]
    return coreRecursive(profits, weights, capacity, 0, dp)


def coreRecursive(profits, weights, capacity, index, dp):
    if index >= len(weights) or capacity <= 0:
        return 0

    if dp[index][capacity] != -1:
        return dp[index][capacity]

    profitNotSkip = 0
    if weights[index] <= capacity:
        profitNotSkip = profits[index] + \
            coreRecursive(profits, weights, capacity -
                          weights[index], index+1, dp)
    profitSkip = coreRecursive(profits, weights, capacity, index+1, dp)

    dp[index][capacity] = max(profitNotSkip, profitSkip)
    return max(profitNotSkip, profitSkip)


# Time (nc)    n*c 个可能
# Space (nc)     n*c 的辅助空间

def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()
