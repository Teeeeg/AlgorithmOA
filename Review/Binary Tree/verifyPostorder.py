from typing import List


class Solution:

    def verifyPostorder(self, postorder: List[int]) -> bool:
        if not postorder:
            return True

        rootVal = postorder[-1]
        leftTreeLen = 0

        for num in postorder:
            if num < rootVal:
                leftTreeLen += 1
            if num > rootVal:
                break

        leftPostorder = postorder[:leftTreeLen]
        rightPostorder = postorder[leftTreeLen:-1]

        for num in rightPostorder:
            if num < rootVal:
                return False

        return self.verifyPostorder(leftPostorder) and self.verifyPostorder(rightPostorder)


postorder = [1, 6, 3, 2, 5]
postorder1 = [1, 3, 2, 6, 5]
slt = Solution()
print(slt.verifyPostorder(postorder))
print(slt.verifyPostorder(postorder1))
