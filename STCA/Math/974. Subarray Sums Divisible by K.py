from typing import List


class Solution:

    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixMod = {0: 1}
        total = 0
        res = 0

        for num in nums:
            total += num
            mod = total % k

            res += prefixMod.get(mod, 0)
            prefixMod[mod] = prefixMod.get(mod, 0) + 1

        return res