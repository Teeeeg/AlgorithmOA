from typing import List


class Solution:

    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        # opt[i][j] means maximum score a ahead of j
        opt = [[0] * n for _ in range(n)]
        # last stone, a get ahead of b for nums[i] score
        for i in range(n):
            opt[i][i] = nums[i]

        for length in range(2, n + 1):
            # i is the start point
            for i in range(n - length + 1):
                # j is the end point
                j = i + length - 1
                # opt[i + 1][j] is the diff of player b
                opt[i][j] = max(nums[i] - opt[i + 1][j], nums[j] - opt[i][j - 1])

        return opt[0][-1] >= 0


nums = [1, 5, 2, 3]
slt = Solution()
print(slt.PredictTheWinner(nums))