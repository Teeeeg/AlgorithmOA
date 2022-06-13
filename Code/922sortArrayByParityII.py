from typing import List


class Solution:

    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for slow in range(n):
            if nums[slow] % 2 != (slow + 2) % 2:
                fast = slow + 1
                while not (fast < n and nums[fast] % 2 != fast % 2 and nums[fast] % 2 == (slow + 2) % 2):
                    fast += 1
                nums[fast], nums[slow] = nums[slow], nums[fast]

        return nums

    def sortArrayByParityII1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        p1 = 1
        p2 = 0

        for i in range(n):
            if nums[i] % 2:
                res[p1] = nums[i]
                p1 += 2
            else:
                res[p2] = nums[i]
                p2 += 2

        return res


nums = [3, 1, 4, 2]
slt = Solution()
print(slt.sortArrayByParityII1(nums))