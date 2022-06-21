#-*- coding:utf-8 -*-
"""
题目：
    24. 反转链表
    定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

思路：
    三个指针，使用先指针和后指针辅助调转指针方向

注意：
    将反转后的链表尾节点指向空
    反转中间节点的指向
    将反转后的链表头节点指向中间链表
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        if not head.next:
            return head

        if not head.next.next:
            tmp = head.next
            head.next = None
            tmp.next = head
            return tmp

        pre, cur, lat = head.next.next, head.next, head
        cur.next = lat
        lat.next = None

        while pre.next:
            pre, cur, lat = pre.next, pre, cur
            cur.next = lat

        pre.next = cur
        return pre


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    s = Solution()
    rev = s.reverseList(head)
    print(rev)