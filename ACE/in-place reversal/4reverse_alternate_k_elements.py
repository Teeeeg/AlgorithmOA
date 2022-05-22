from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse_alternate_k_elements(head: Node, k):
    if not head or not head.next:
        return head

    pre = None
    cur = head

    while True:
        tail_of_pre = pre
        tail_of_sub = cur
        i = 0

        while cur and i < k:
            post = cur.next
            cur.next = pre
            pre = cur
            cur = post
            i += 1

        head_of_sub = pre
        head_of_tail = cur

        if tail_of_pre:
            tail_of_pre.next = head_of_sub
        else:
            head = head_of_sub

        tail_of_sub.next = head_of_tail

        # head.print_list()

        # 更新pre，以便下一个循环
        pre = tail_of_sub
        if not cur:
            break

        # 跳过，类似前面
        i = 0
        while cur and i < k:
            tail_of_pre = cur
            cur = cur.next
            i += 1
        pre = tail_of_pre

        if not cur:
            break

    return head


# Time O(n)
# Space O(1)


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)
    head.next.next.next.next.next.next.next.next = Node(9)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_alternate_k_elements(head, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
