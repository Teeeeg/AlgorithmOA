from typing import List


class Solution:

    def combinationSum2Core(self, candidates: List[int], path: List[int], target: int, res: List[List[int]],
                            startIndex):
        # 减枝
        if sum(path) > target:
            return
        # 符合条件的记录
        if sum(path) == target:
            res.append(path[:])

        for i in range(startIndex, len(candidates)):
            # 去重
            if i > startIndex and candidates[i] == candidates[i - 1]:
                continue
            path.append(candidates[i])
            self.combinationSum2Core(candidates, path, target, res, i + 1)
            path.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.combinationSum2Core(candidates, [], target, res, 0)
        return res


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
slt = Solution()
print(slt.combinationSum2(candidates, target))
