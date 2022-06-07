from typing import List


class Solution:

    def singleNumber(self, nums: List[int]) -> int:
        dct = {}
        for num in nums:
            dct[num] = dct.get(num, 0) + 1

        for num, freq in dct.items():
            if freq == 1:
                return num

        return -1

    def singleNumber1(self, nums: List[int]) -> int:
        one = 0
        two = 0

        for num in nums:
            one = one ^ num & (~two)
            two = two ^ num & (~one)

        return one
