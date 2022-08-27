from typing import List


class Solution:

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.subsetsWithDupCore(nums, [], res, 0)
        return res

    def subsetsWithDupCore(self, nums, path, res, startIndex):
        res.append(path[:])

        for i in range(startIndex, len(nums)):
            # 1， 2(1)， 2(2)
            # choose 1， 2(1) first
            # always choose 2(1) then choose 2(2)
            # [0, startIndex) is choosen
            # use i > startIndex indicates haven't been choosen
            # when comes to 2(1)， 2(2), choose 2(1) first
            if i > startIndex and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            self.subsetsWithDupCore(nums, path, res, i + 1)
            path.pop()