from typing import List


class Solution:
    # 【左，右，中】
    # 遍历获取第一个比最后一个大的节点
    # 则由此可分为左右，分治
    def verifyPostorder(self, postorder: List[int]) -> bool:
        # base case
        if not postorder:
            return True

        n = len(postorder)
        i = 0
        # 获取切分位
        while i < n - 1 and postorder[i] < postorder[-1]:
            i += 1
        sepIndex = i

        # 分，分别分入左右子树处理
        if not self.verifyPostorder(postorder[:i]):
            return False
        if not self.verifyPostorder(postorder[i:-1]):
            return False
        # 治，判断每个片段里是否满足条件
        i = 0
        while i < n - 1:
            # 左子树都比root小
            if i < sepIndex:
                if postorder[i] > postorder[-1]:
                    return False
            # 右子树都比root大
            if i >= sepIndex:
                if postorder[i] < postorder[-1]:
                    return False
            i += 1

        return True


postorder = [1, 6, 3, 2, 5]
slt = Solution()
print(slt.verifyPostorder(postorder))
