from typing import List


class Solution:

    def lastStoneWeightII(self, stones: List[int]) -> int:
        if not stones:
            return 0

        total = sum(stones)
        target = total // 2
        # opt[i] means the maximum stone it can store in a bag capacity of i
        opt = [0] * (target + 1)

        for stone in stones:
            # bigger bagpack relies on smaller backpack
            for i in range(target, stone - 1, -1):
                opt[i] = max(opt[i], opt[i - stone] + stone)

        return total - 2 * opt[-1]