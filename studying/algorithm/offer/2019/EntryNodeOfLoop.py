# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead or not pHead.next or not pHead.next.next:
            return None
        f, s = pHead.next.next, pHead.next
        while not not f and not not s and f != s:
            f = f.next.next if f.next and f.next.next else None
            s = s.next if s.next else None
        if not f or not s or f != s:
            return None
        f = pHead
        while f != s:
            f = f.next
            s = s.next
        return f
