# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur1 = l1
        cur2 = l2
        dummyHead = ListNode(0)
        cur = dummyHead
        carry = 0

        while cur1 or cur2:
            digit1 = 0
            digit2 = 0
            if cur1:
                digit1 = cur1.val
                cur1 = cur1.next
            if cur2:
                digit2 = cur2.val
                cur2 = cur2.next

            total = digit1 + digit2 + carry
            carry = total // 10
            cur.next = ListNode(total % 10)  # type: ignore
            cur = cur.next

        # 注意最后的进位
        if carry:
            cur.next = ListNode(1)  # type: ignore

        return dummyHead.next  # type: ignore
