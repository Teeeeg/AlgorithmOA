# Definition for singly-linked list.
from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 对半切分
    def sepList(self, head: Optional[ListNode]):
        if not head:
            return head
        # 利用dummyHead切开
        # 最后slow.next指向的是后半部分的head
        dummyHead = ListNode(next=head)
        slow = fast = dummyHead

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 断开连接
        res = slow.next
        slow.next = None  # type: ignore

        return res

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base Case
        if not head or not head.next:
            return head

        leftHead = head
        rightHead = self.sepList(head)

        # 递归
        # 归并的思想是分治
        # 因此先用递归分， 递归后再治
        left = self.sortList(leftHead)
        right = self.sortList(rightHead)

        # 递归内执行内容
        # 治的过程
        dummyHead = ListNode(0)
        cur = dummyHead
        # 分别连接最小的
        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        # 最后处理剩余的
        if left:
            cur.next = left
        if right:
            cur.next = right
        return dummyHead.next
