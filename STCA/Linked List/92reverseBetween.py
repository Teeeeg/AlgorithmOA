# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head:
            return head

        dummyHead = ListNode(next=head)
        pre = None
        cur = dummyHead

        # cur遍历到要被翻转的链表头
        for _ in range(left):
            pre = cur
            cur = pre.next

        # 记录断开的节点
        tailOfSub = cur
        tailOfPre = pre

        # 正常翻转操作
        pre = None
        for _ in range(right - left + 1):
            post = cur.next
            cur.next = pre
            pre = cur
            cur = post

        # 记录尾部断点
        headOfSub = pre
        headOfPost = cur

        # 连接
        if tailOfPre:
            tailOfPre.next = headOfSub

        tailOfSub.next = headOfPost

        return dummyHead.next
