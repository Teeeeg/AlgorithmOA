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


def reverse_sub_list(head: Node, p, q):
    pre = None
    cur = head

    # 从head出发要少遍历一次
    for _ in range(p-1):
        pre = cur
        cur = cur.next

    tail_of_sub = cur
    tail_of_pre = pre

    pre = None
    for _ in range(q-p+1):
        post = cur.next
        cur.next = pre
        pre = cur
        cur = post
    first_of_sub = pre
    first_of_tail = cur

    # 前一段的尾节点为空，则为翻转第一个
    if tail_of_pre:
        tail_of_pre.next = first_of_sub
    else:
        head = first_of_sub

    tail_of_sub.next = first_of_tail

    return head


# Time O(n)
# Space O(1)

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_sub_list(head, 2, 4)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
