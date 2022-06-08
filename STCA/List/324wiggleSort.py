from typing import List


class Solution:
    # 排好序，从中间穿插

    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)
        cloned = nums[:]
        cloned.sort()
        left = (n - 1) // 2
        right = n - 1

        for i in range(n):
            # 用取余数的方法穿插
            if i % 2 == 0:
                nums[i] = cloned[left]
                left -= 1
            else:
                nums[i] = cloned[right]
                right -= 1

    def wiggleSort1(self, nums: List[int]) -> None:
        # 因为题目限定数的大小
        # 桶排序
        buckets = [0] * 5001
        n = len(nums)
        for num in nums:
            buckets[num] += 1

        j = 5000
        # 穿插大的
        for i in range(1, n, 2):
            while buckets[j] == 0:
                j -= 1
            nums[i] = j
            buckets[j] -= 1
        # 穿插小的
        for i in range(0, n, 2):
            while buckets[j] == 0:
                j -= 1
            nums[i] = j
            buckets[j] -= 1


nums = [1, 5, 1, 1, 6, 4]
slt = Solution()
slt.wiggleSort(nums)
print(nums)
