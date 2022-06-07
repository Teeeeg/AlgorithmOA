from typing import List


class Solution:

    def getCount(self, nums: List[int], index):
        # 应该的数字应该是起始数字+偏移量
        realNum = index + nums[0]
        # 缺失的数量
        return nums[index] - realNum

    # 不同于一般的二分
    # 最终要返回left
    def binarySearch(self, nums: List[int], k):
        n = len(nums)
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            count = self.getCount(nums, mid)
            # 返回上限
            if left < mid < right and self.getCount(nums, mid + 1) < count < self.getCount(nums, mid + 1):
                return mid

            if count < k:
                left = mid + 1
            else:
                right = mid - 1
        # 否则返回上限left
        return right

    def missingElement(self, nums: List[int], k: int) -> int:
        index = self.binarySearch(nums, k)
        # 最终答案应该是上一个节点 + 偏移 - 上一个节点已经的偏移
        res = nums[index] + k - self.getCount(nums, index)

        return res


nums = [6, 7, 10, 11, 19, 21, 23]
k = 2
slt = Solution()
print(slt.missingElement(nums, k))
