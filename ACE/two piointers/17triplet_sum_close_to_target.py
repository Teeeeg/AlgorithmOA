import math


def triplet_sum_close_to_target(arr, target_sum):
    n = len(arr)
    arr.sort()
    smallest = math.inf

    for i in range(n-2):
        l, r = i+1, n-1
        while l < r:
            triple = arr[i] + arr[l] + arr[r]
            diff = target_sum - triple
            if diff == 0:
                return target_sum

            # 距离一样的情况只可能绝对值相同的两个不同值
            # diff是正数代表triple一定小雨target，此前smallest可能为target右侧的值，为负数
            if abs(diff) < abs(smallest) or (abs(diff) == abs(smallest) and diff > smallest):
                smallest = diff

            if diff > 0:
                l += 1
            else:
                r -= 1

    return target_sum-smallest

# 排序O(nlogn)
# for嵌套一个while为O(n2)
# 总体O(n2)

# O(n)用于排序


arr = [-3, -1, 1, 2]
target = 1
print(triplet_sum_close_to_target(arr, target))
