def find_subsets(nums):
    subsets = []
    subsets.append([])

    for num in nums:
        # 当前队列长度
        n = len(subsets)
        for i in range(n):
            # 广度优先
            # 将每一个subset追加新num再放回去
            new_subset = subsets[i][:]
            new_subset.append(num)
            subsets.append(new_subset)

    return subsets


# 节点数类似二叉树分裂
# 而每个节点最大可能为N

# Time O(n*2^n)
# Space O(n*2^n)

def main():

    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()
