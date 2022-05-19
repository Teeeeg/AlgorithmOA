from typing import List


class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # 排序是为了剪枝
        candidates.sort()
        self.combinationSumCore(candidates, [], res, target, 0)
        return res

    def combinationSumCore(self, candidates: List[int], path: List, res: List, target, startIndex):
        if target < 0:
            return

        if target == 0:
            res.append(path[:])

        for i in range(startIndex, len(candidates)):
            # 若减去下一个元素小于0，则不可能使target = 0
            # candidates 已经排过序
            if target - candidates[i] < 0:
                return
            path.append(candidates[i])
            self.combinationSumCore(candidates, path, res, target - candidates[i], i)
            path.pop()


candidates = [2, 3, 5]
target = 8
slt = Solution()
print(slt.combinationSum(candidates, target))
