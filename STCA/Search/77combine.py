from typing import List


class Solution:

    def combineCore(self, n, k, path, startIndex):
        if len(path) == k:
            self.res.append(path[:])
            return
        # need a number of k - len(path)
        # start at most from n + 1 - (k-len(path))
        # python [), so +1 in the end
        for i in range(startIndex, n - k + len(path) + 2):
            path.append(i)
            self.combineCore(n, k, path, i + 1)
            path.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        self.combineCore(n, k, [], 1)
        return self.res


slt = Solution()
print(slt.combine(4, 2))