from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        res[0] = self.binaySearch(nums, target, True)
        if res[0] == -1:
            return res
        res[1] = self.binaySearch(nums, target, False)
        return res

    def binaySearch(self, nums: List, target, findLeft):
        n = len(nums)
        start, end = 0, n-1
        findLeft = findLeft
        res = -1

        while start <= end:
            mid = (start+end) // 2
            if nums[mid] == target:
                res = mid
                if findLeft:
                    end = mid-1
                else:
                    start = mid+1

            if nums[mid] < target:
                start = mid+1
            elif nums[mid] > target:
                end = mid-1
        return res


nums = [2, 2]
target = 2
solution = Solution()
print(solution.searchRange(nums, target))
