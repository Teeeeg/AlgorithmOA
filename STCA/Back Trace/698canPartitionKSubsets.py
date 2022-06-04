from typing import List


class Solution:

    def canPartitionKSubsetsCore(self, nums: List[int], k: int, buckets: List[int], index, target):
        n = len(nums)
        if index == n:
            return True

        for i in range(k):
            # 剪枝
            if nums[index] + buckets[i] > target:
                continue
            # 上一个桶和现在相同，则结果一样
            if i > 0 and buckets[i - 1] == buckets[i]:
                continue

            buckets[i] += nums[index]
            if self.canPartitionKSubsetsCore(nums, k, buckets, index + 1, target):
                return True
            # 回溯
            buckets[i] -= nums[index]

        return False

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # 预处理
        total = sum(nums)
        if total % k:
            return False

        target = total // k
        buckets = [0] * k
        # 先放大的再放小的
        nums.sort(reverse=True)

        return self.canPartitionKSubsetsCore(nums, k, buckets, 0, target)


nums = [3, 9, 4, 5, 8, 8, 7, 9, 3, 6, 2, 10, 10, 4, 10, 2]
k = 10
slt = Solution()
print(slt.canPartitionKSubsets(nums, k))