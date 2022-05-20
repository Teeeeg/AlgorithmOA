from typing import Any


class TreeNode:

    def __init__(self, val=0, left=Any, right=Any, next=Any):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:

    def getNext(self, root: TreeNode):
        # 如果有有右子树
        # 则下一个节点就是右子树的最左节点
        if root.right:
            cur = root.right
            while cur.left:
                cur = cur.left
            return cur

        # 若无右子树
        # 则一直向上遍历
        # 找到当前节点是其父节点的节点
        # 则该节点的父节点即是答案
        cur = root
        while cur.next:
            if cur.next.left == cur:
                return cur.next
            cur = cur.next

        return None


root = TreeNode(1)
t1 = TreeNode(2)
t2 = TreeNode(3)
root.left = t1
root.right = t2
t1.next = root
t2.next = root
t3 = TreeNode(4)
t4 = TreeNode(5)
t1.left = t3
t1.right = t4
t3.next = t1
t4.next = t1
t5 = TreeNode(7)
t3.left = t5
t5.next = t3
t6 = TreeNode(8)
t7 = TreeNode(9)
t4.left = t6
t4.right = t7
t6.next = t4
t7.next = t4

slt = Solution()
res = slt.getNext(t4)