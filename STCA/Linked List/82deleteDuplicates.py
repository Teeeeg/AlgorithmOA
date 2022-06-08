# Definition for singly-linked list.


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 递归
    # 自顶向下

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 当前为空或只有一个
        if not head or not head.next:
            return head
        # 若当前不相等
        # 考虑它后面的
        if head.val != head.next.val:
            # 接在它后面
            head.next = self.deleteDuplicates(head.next)
        else:
            # 若现在相等
            # 则一直向后找到不相等的
            nextHead = head.next
            while nextHead and head.val == nextHead.val:
                nextHead = nextHead.next

            return self.deleteDuplicates(nextHead)

        return head

    def deleteDuplicates1(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # 用虚拟头节点，方便处理第一个重复的情况
        dummyHead = ListNode(next=head)
        pre = dummyHead
        cur = dummyHead.next

        while cur:
            # 让cur一直向后找到第一个不重复的节点
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            # 若cur没有移动，说明该节点不重复，则保留
            if pre.next == cur:
                pre = cur
            else:
                # 跳过这个重复的一块
                # 则结果指针指向下一段的开始
                pre.next = cur.next
            cur = cur.next

        return dummyHead.next
