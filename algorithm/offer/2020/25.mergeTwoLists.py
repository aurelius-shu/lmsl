#-*- coding:utf-8 -*-
"""
题目：
    25. 合并两个排序的链表
    输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

思路：
挨个遍历两个链表，比较大小，取小的链表放到新链表中

注意：
两个链表分别为空的情况
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return l1

        if not l1:
            headval = l2.val
            l2 = l2.next
        elif not l2:
            headval = l1.val
            l1 = l1.next
        elif l1.val > l2.val:
            headval = l2.val
            l2 = l2.next
        else:
            headval = l1.val
            l1 = l1.next

        head = ListNode(headval)
        cur = head

        while l1 or l2:
            if not l1:
                cur.next = l2
                l2 = None
            elif not l2:
                cur.next = l1
                l1 = None
            elif l1.val > l2.val:
                cur.next = ListNode(l2.val)
                cur = cur.next
                l2 = l2.next
            else:
                cur.next = ListNode(l1.val)
                cur = cur.next
                l1 = l1.next

        return head


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    s = Solution()
    res = s.mergeTwoLists(l1, l2)
    print(res)