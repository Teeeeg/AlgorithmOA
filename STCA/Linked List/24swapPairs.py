# Definition for singly-linked list.
from turtle import right


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 多用指针记录
    def swapPairs(self, head: ListNode) -> ListNode:
        # base case
        if not head:
            return head
        # 用dummyHead因为方便修改前两个元素
        dummyHead = ListNode(next=head)
        cur = dummyHead

        while cur.next and cur.next.next:
            # 分别记录四个指针
            pre = cur
            left = cur.next
            right = cur.next.next
            post = cur.next.next.next
            # 连接
            pre.next = right
            right.next = left
            left.next = post
            # 最后更新cur
            # left变成下一段的前一个
            cur = left

        return dummyHead.next
