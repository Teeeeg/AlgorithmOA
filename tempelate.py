def test_multi_pack1():
    weight = [1, 3, 4]
    value = [15, 20, 30]
    nums = [2, 3, 2]
    bag_weight = 10
    for i in range(len(nums)):
        # 将物品展开数量为1
        while nums[i] > 1:
            weight.append(weight[i])
            value.append(value[i])
            nums[i] -= 1

    dp = [0]*(bag_weight + 1)
    # 遍历物品
    for i in range(len(weight)):
        # 遍历背包
        for j in range(bag_weight, weight[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

    print(" ".join(map(str, dp)))


def test_multi_pack2():
    '''版本：改变遍历个数'''
    weight = [1, 3, 4]
    value = [15, 20, 30]
    nums = [2, 3, 2]
    bag_weight = 10

    dp = [0]*(bag_weight + 1)
    for i in range(len(weight)):
        for j in range(bag_weight, weight[i] - 1, -1):
            # 以上是01背包，加上遍历个数
            for k in range(1, nums[i] + 1):
                if j - k*weight[i] >= 0:
                    dp[j] = max(dp[j], dp[j - k*weight[i]] + k*value[i])

    print(" ".join(map(str, dp)))


test_multi_pack2()
