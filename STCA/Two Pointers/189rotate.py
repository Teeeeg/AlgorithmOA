from typing import List


class Solution:

    def rerverse(self, nums, left, right):
        if left > right:
            return

        while left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        # k取余数
        k %= n
        # 整体翻转
        self.rerverse(nums, 0, n - 1)
        # 翻转前半部分
        self.rerverse(nums, 0, k - 1)
        # 翻转后半部分
        self.rerverse(nums, k, n - 1)


nums = [-1]
k = 2
slt = Solution()
slt.rotate(nums, k)
print(nums)