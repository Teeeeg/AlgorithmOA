def find_subsets(nums):
    subsets = []
    nums.sort()
    subsets.append([])

    # 重复项产生于
    # [], [1], [3], [1,3]
    # [3], [1,3],          [3,3], [1,3,3]]
    for i in range(len(nums)):
        # 发现重复则跳过
        startIndex = 0
        if i > 0 and nums[i-1] == nums[i]:
            startIndex += 1
        # 从不重复的开始，把新的加进去
        for j in range(startIndex, len(subsets)):
            new_subset = subsets[j][:]
            new_subset.append(nums[i])
            subsets.append(new_subset)

    return subsets


# Time O(n*2^n)
# Space O(n*2^n)

def main():

    print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()
