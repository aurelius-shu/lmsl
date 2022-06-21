# -*- coding:utf-8 -*-

# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None
        cur = pHead
        while cur:
            node = RandomListNode(cur.label)
            node.next = cur.next
            cur.next = node
            cur = node.next
        cur = pHead
        while cur:
            cur.next.random = cur.random
            cur = cur.next.next
        cur = pHead
        pClone = pHead.next
        while cur.next:
            next = cur.next
            cur.next = next.next
            cur = next
        return pClone
