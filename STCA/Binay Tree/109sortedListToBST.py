# Definition for singly-linked list.
from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return head
        # 当只有一个节点的时候返回节点
        if not head.next:
            return TreeNode(head.val)

        dummyHead = ListNode(next=head)
        slow = fast = dummyHead
        # 用于断开mid-1与mid
        pre = None

        # 找到中间节点
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        # 后一段
        postHead = slow.next
        root = TreeNode(slow.val)
        pre.next = None  # type: ignore
        # pre无法断开head

        # 一定要dummyHead.next
        root.left = self.sortedListToBST(dummyHead.next)  # type: ignore
        root.right = self.sortedListToBST(postHead)  # type: ignore

        return root
