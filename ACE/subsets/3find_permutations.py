def find_permutations(nums):
    res = []
    n = len(nums)
    permutations = []
    permutations.append([])

    # 类似排列，最后达到组合的长度时记录结果
    for num in nums:
        n1 = len(permutations)
        for _ in range(n1):
            # 取出上一轮的组合
            # 用pop，因为不需要保存上一轮的数据，迭代而不是附加
            pre = permutations.pop(0)
            # 有len+1个位置可以插入
            for j in range(len(pre)+1):
                cur = pre[:]
                cur.insert(j, num)
                # 当达到组合时候，记录结果
                if len(cur) == n:
                    res.append(cur)
                # 否则继续下一轮
                else:
                    permutations.append(cur)

    return res

# Time O(n*n!)
# Space O(n*n!)


def main():
    print("Here are all the permutations: " +
          str(find_permutations([1, 3, 5])))


main()
