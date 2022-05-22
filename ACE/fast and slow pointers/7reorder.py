from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.value) + " ", end='')
            temp = temp.next
        print()


def reorder(head):
    def reverseList(head: Node):
        if not head or not head.next:
            return head
        pre = None
        cur = head
        while cur:
            post = cur.next
            cur.next = pre
            pre = cur
            cur = post
        return pre

    dummyHead = Node(0, head)
    slow = fast = dummyHead
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    midNode = slow.next
    slow.next = None
    reversedHead = reverseList(midNode)
    cur1 = head
    cur2 = reversedHead

    while cur1 and cur2:
        tmp1 = cur1.next
        tmp2 = cur2.next

        cur1.next = cur2
        cur2.next = tmp1
        cur1 = tmp1
        cur2 = tmp2

    return dummyHead.next


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(12)

    reorder(head)
    head.print_list()


main()
