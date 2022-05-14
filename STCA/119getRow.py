from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]

        n = rowIndex+1
        pre = [1, 1]

        for i in range(1, n):
            cur = [1] * (i+1)
            for i in range(1, len(cur)-1):
                cur[i] = pre[i-1]+pre[i]
            pre = cur

        return pre


s = Solution()
print(s.getRow(4))
