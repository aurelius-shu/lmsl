# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        p1, p2 = pHead1, pHead2
        while p1.val != p2.val:
            p1 = p1.next if p1.next != None else pHead2
            p2 = p2.next if p2.next != None else pHead1
        return p1
