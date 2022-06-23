from typing import List


class Sort:

    def bubbleSort(self, nums: List[int]):
        n = len(nums)

        for i in range(n):
            for j in range(n - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j + 1], nums[j] = nums[j], nums[j + 1]

        return nums


nums = [5, 2, 1, 2, 5, 2, 1]
sort = Sort()
print(sort.bubbleSort(nums))