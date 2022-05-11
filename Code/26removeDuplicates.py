from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0

        for right in range(n):
            if nums[left] == nums[right]:
                continue
            if left != right:
                left += 1
                nums[left], nums[right] = nums[right], nums[left]

        return left+1


nums = [1, 1, 2]
solution = Solution()
print(solution.removeDuplicates(nums))
