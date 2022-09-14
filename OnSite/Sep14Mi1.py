#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


class ListNode:

    def __init__(self):
        self.data = None
        self.next = None


class Solution:

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head:
            return head

        pre = None
        cur = head

        # cur遍历到要被翻转的链表头
        for _ in range(left - 1):
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
        else:
            head = headOfSub

        tailOfSub.next = headOfPost

        return head


head_cnt = int(input())
head = None
head_curr = None
for _ in range(head_cnt):
    x = int(input())
    head_temp = ListNode()
    head_temp.data = int(x)
    head_temp.next = None
    if head == None:
        head = head_temp
        head_curr = head
    else:
        head_curr.next = head_temp
        head_curr = head_temp

left = int(input())
right = int(input())

s = Solution()
res = s.reverseBetween(head, left, right)

while res != None:
    print(str(res.data), end=" ")
    res = res.next
