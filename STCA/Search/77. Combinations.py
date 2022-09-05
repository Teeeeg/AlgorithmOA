from typing import List


class Solution:

    def combineCore(self, n: int, k: int, startIndex: int, path: List[int]):
        if len(path) == k:
            self.res.append(list(path))
            return

        for i in range(startIndex, n - k + len(path) + 2):
            self.combineCore(n, k, i + 1, path + [i])

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        self.combineCore(n, k, 1, [])

        return self.res


n = 1
k = 1
slt = Solution()
print(slt.combine(n, k))
