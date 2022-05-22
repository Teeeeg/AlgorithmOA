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

# 需要更新这几个指针
# tail_of_sub
# tail_of_pre
# first_of_sub
# first_of_tail
# cur   当前
# pre   前一个指针


def reverse_every_k_elements(head, k):
    if k <= 1 or head is None:
        return head

    pre = None
    cur = head

    while True:
        tail_of_sub = cur
        tail_of_pre = pre
        i = 0

        # 翻转k个
        while cur and i < k:
            post = cur.next
            cur.next = pre
            pre = cur
            cur = post
            i += 1
        first_of_sub = pre
        first_of_tail = cur

        if tail_of_pre:
            tail_of_pre.next = first_of_sub
        else:
            head = first_of_sub

        tail_of_sub.next = first_of_tail

        # 则pre是sub的尾节点
        pre = tail_of_sub
        # 当前cur不存在，则返回
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

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_every_k_elements(head, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
