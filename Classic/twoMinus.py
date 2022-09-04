def printList(head):
    res = []
    while head:
        res.append(head.value)
        head = head.next

    print(res)


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:

    def reverse(self, head: Node) -> Node:
        pre = None
        cur = head

        while cur:
            post = cur.next
            cur.next = pre
            pre = cur
            cur = post

        return pre  # type: ignore

    def twoMinus(self, headA: Node, headB: Node):
        curA = self.reverse(headA)
        curB = self.reverse(headB)
        carry = 0
        resHead = Node(0)
        cur = resHead

        while curA or curB:
            digitA = 0
            if curA:
                digitA = curA.value
                curA = curA.next

            digitB = 0
            if curB:
                digitB = curB.value
                curB = curB.next

            digit = digitA - digitB + carry
            if digit > 0:
                cur.next = Node(digit)
            elif digit < 0:
                cur.next = Node(digit + 10)
                carry = -1
            else:
                cur.next = Node(digit)

            cur = cur.next

        return self.reverse(resHead.next)


headA = Node(3)
headA.next = Node(2)
headA.next.next = Node(2)

headB = Node(1)
headB.next = Node(2)

printList(headA)
printList(headB)

slt = Solution()
res = slt.twoMinus(headA, headB)
printList(res)