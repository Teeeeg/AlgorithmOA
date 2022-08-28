from typing import List


class Solution:

    def mergeTwo(self, nums: List[int], left, mid, right):
        tmp = []
        l = left
        r = mid + 1

        while l <= mid and r <= right:
            if nums[l] <= nums[r]:
                tmp.append(nums[l])
                l += 1
            else:
                tmp.append(nums[r])
                r += 1

        while l <= mid:
            tmp.append(nums[l])
            l += 1

        while r <= right:
            tmp.append(nums[r])
            r += 1

        nums[left:right + 1] = tmp[:]

    def mergeSortCore(self, nums: List[int], left, right):
        if left >= right:
            return

        mid = (left + right) >> 1
        self.mergeSortCore(nums, left, mid)
        self.mergeSortCore(nums, mid + 1, right)
        self.countPairs(nums, left, mid, right)
        self.mergeTwo(nums, left, mid, right)

    def mergeSort(self, nums: List[int]):
        if not nums:
            return
        n = len(nums)
        self.mergeSortCore(nums, 0, n - 1)

    def countPairs(self, nums: List[int], left, mid, right):
        # count satisfied pairs
        index = mid + 1

        for num in nums[left:mid + 1]:
            # index grows to 2 * nums[index] >= num
            while index <= right and 2 * nums[index] < num:
                index += 1
            # count will be index - mid - 1
            self.count += index - mid - 1

    def reversePairs(self, nums: List[int]) -> int:
        # merge sort
        # in every segment, count pairs
        self.count = 0
        self.mergeSort(nums)
        return self.count


nums = [2, 4, 3, 5, 1]
slt = Solution()
print(slt.reversePairs(nums))