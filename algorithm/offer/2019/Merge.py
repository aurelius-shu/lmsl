# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1

            if pHead1.val < pHead2.val:
                pHead = ListNode(pHead1.val)
                pHead1 = pHead1.next
            else:
                pHead = ListNode(pHead2.val)
                pHead2 = pHead2.next

            curNode = pHead
            while pHead1 or pHead2:
                if not pHead2:
                    curNode.next = ListNode(pHead1.val)
                    pHead1 = pHead1.next
                elif not pHead1:
                    curNode.next = ListNode(pHead2.val)
                    pHead2 = pHead2.next
                elif pHead1.val < pHead2.val:
                    curNode.next = ListNode(pHead1.val)
                    pHead1 = pHead1.next
                elif pHead1.val >= pHead2.val:
                    curNode.next = ListNode(pHead2.val)
                    pHead2 = pHead2.next

                curNode = curNode.next
            return pHead