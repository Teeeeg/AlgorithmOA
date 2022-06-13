from typing import List


class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
slt = Solution()
slt.rotate(nums, k)
print(nums)