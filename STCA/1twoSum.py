from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}

        for i in range(len(nums)):
            if target-nums[i] in dct:
                return [i, dct[target-nums[i]]]
            else:
                dct[nums[i]] = i

        return [-1, -1]
