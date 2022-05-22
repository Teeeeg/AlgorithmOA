class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def is_palindromic_linked_list(head: Node):
    def reverseList(head: Node) -> Node:
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
    reversedHead = reverseList(midNode)
    reverseCopy = reversedHead

    cur1 = head
    cur2 = reverseCopy

    while cur1 and cur2:
        if cur1.value != cur2.value:
            break
        cur1 = cur1.next
        cur2 = cur2.next

    reverseList(reverseCopy)

    if not cur1 or not cur2:
        return True

    return False


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Is palindrome: " + str(is_palindromic_linked_list(head)))

    head.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()

# Time O(n)
# O(1)
