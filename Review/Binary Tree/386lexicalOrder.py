from typing import List


class Solution:
    # just pre-order traversal 9-tree

    def lexicalOrderCore(self, i, n, res):
        # base case
        if i > n:
            return
        # pre-order logic
        res.append(i)
        # define next iteration boundries
        leftBound = i * 10
        rightBound = min(i * 10 + 9, n)

        for i in range(leftBound, rightBound + 1):
            self.lexicalOrderCore(i, n, res)

    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        # inital status
        leftBound = 1
        rightBound = min(9, n)

        for i in range(leftBound, rightBound):
            self.lexicalOrderCore(i, n, res)

        return res
