from typing import List


class Solution:

    def lexicalOrderCore(self, root: int, n, res: List[int]):
        if root > n:
            return

        res.append(root)

        if root * 10 > n:
            return

        for child in range(root * 10, min(n + 1, root * 10 + 10)):
            self.lexicalOrderCore(child, n, res)

    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        for root in range(1, min(10, n + 1)):
            self.lexicalOrderCore(root, n, res)

        return res


n = 13
slt = Solution()
print(slt.lexicalOrder(n))