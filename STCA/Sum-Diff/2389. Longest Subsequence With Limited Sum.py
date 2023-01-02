from typing import List


class Solution:

    def binarySearch(self, nums: List[int], target: int):
        left = 0
        right = len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid

        if nums[right] <= target:
            return right
        return left

    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        sortedNums = sorted(nums)
        prefixSum = [0]

        for num in sortedNums:
            prefixSum.append(prefixSum[-1] + num)

        res = []

        for query in queries:
            res.append(self.binarySearch(prefixSum, query))

        return res


nums = [4, 5, 2, 1]
queries = [3, 10, 21]
slt = Solution()
print(slt.answerQueries(nums, queries))
