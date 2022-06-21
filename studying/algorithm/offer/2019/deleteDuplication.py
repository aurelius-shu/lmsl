# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead:
            return pHead
        pre, cur, next = None, pHead, pHead.next
        while next:
            if cur.val == next.val:
                while next.next and next.val == next.next.val:
                    next = next.next
                if next.val == pHead.val:
                    pHead = next.next
                else:
                    pre.next = next.next
                cur, next = next.next, next.next.next if next.next else None
            else:
                pre, cur, next = cur, next, next.next

        return pHead
