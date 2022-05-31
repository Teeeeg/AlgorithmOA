from typing import List


class Solution:
    # 找最左边的最小数 和 右边的最大数
    # 即从后往前，第一个递增的为最小数，从后往前第一个比最小数大的为最大数
    # 两个交换
    # 最后讲最小数后面的数全部反转
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)

        leftIndex = -1
        rightIndex = -1
        # 寻找最小数
        for i in range(n - 2, -1, -1):
            # 第一个递增
            if nums[i] < nums[i + 1]:
                leftIndex = i
                break
        # 表明整个数组递减
        # 返回反转的
        if leftIndex == -1:
            return nums.reverse()
        # 寻找最大数
        for i in range(n - 1, leftIndex, -1):
            # 第一个比最小数大的
            if nums[i] > nums[leftIndex]:
                rightIndex = i
                break

        nums[leftIndex], nums[rightIndex] = nums[rightIndex], nums[leftIndex]
        nums[leftIndex + 1:] = reversed(nums[leftIndex + 1:])


nums = [1, 3, 2]
slt = Solution()
slt.nextPermutation(nums)
print(nums)
