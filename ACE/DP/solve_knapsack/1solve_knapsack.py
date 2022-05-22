# 回归
def solve_knapsack(profits, weights, capacity):
    return coreRecursive(profits, weights, capacity, 0)


def coreRecursive(profits, weights, capacity, index):
    if index >= len(weights) or capacity <= 0:
        return 0

    profitNotSkip = 0
    if weights[index] <= capacity:
        profitNotSkip = profits[index] + \
            coreRecursive(profits, weights, capacity-weights[index], index+1)
    profitSkip = coreRecursive(profits, weights, capacity, index+1)

    return max(profitNotSkip, profitSkip)


# Time (2^n)    二叉树
# Space (n)     递归栈

def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()
