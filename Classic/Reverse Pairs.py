from typing import List


class Solution:

    def mergeTwo(self, nums: List[int], left: int, mid: int, right: int):
        tmp = [0] * (right - left + 1)
        l = left
        r = mid + 1
        i = 0

        while l <= mid and r <= right:
            if nums[l] <= nums[r]:
                tmp[i] = nums[l]
                l += 1
            else:
                tmp[i] = nums[r]
                r += 1
            i += 1

        while l <= mid:
            tmp[i] = nums[l]
            l += 1
            i += 1

        while r <= right:
            tmp[i] = nums[r]
            r += 1
            i += 1

        nums[left:right + 1] = tmp

    def mergeCore(self, nums: List[int], left: int, right: int):
        if left >= right:
            return

        mid = (left + right) // 2

        self.mergeCore(nums, left, mid)
        self.mergeCore(nums, mid + 1, right)
        # count it from sorted lists
        self.countPairs(nums, left, mid, right)
        self.mergeTwo(nums, left, mid, right)

    def countPairs(self, nums: List[int], left: int, mid: int, right: int):
        index = mid + 1

        for num in nums[left:mid + 1]:
            while index <= right and num > 2 * nums[index]:
                index += 1
            # index - start point
            self.count += index - (mid + 1)

    def reversePairs(self, nums: List[int]) -> int:
        self.count = 0
        self.mergeCore(nums, 0, len(nums) - 1)

        return self.count


nums = [1, 3, 2, 3, 1]
slt = Solution()
print(slt.reversePairs(nums))