#!/usr/bin/env python3
# -*- coding:utf-8 -*-


'''
56. 链表中环的入口结点

1. 找到环的结点数n：一快一慢两个指针相遇，得到环中某个结点，再从此结点沿环一圈，得到环的结点数n
2. 设置两个指针，一个先走n步，两个指针同速前行，当两个指针相遇，即使环的入口结点
'''

from LinkList import ListNode


def entry_node_of_loop(listHead):
    if not listHead:
        return None
    meetingnode = meeting_node(listHead)
    if not meetingnode:
        return None

    # 环中结点个数
    nodesinloop = 1
    p = meetingnode
    while p.next.value != meetingnode.value:
        p = p.next
        nodesinloop += 1

    p1, p2 = listHead, listHead
    for i in range(nodesinloop):
        p1 = p1.next

    while p1.value != p2.value:
        p1 = p1.next
        p2 = p2.next
    return p1


def meeting_node(listHead):
    if listHead.next:
        slow = listHead.next
    if slow.next:
        fast = slow.next

    while slow and fast:
        if slow.value == fast.value:
            return fast
        if slow.next:
            slow = slow.next
        if fast.next:
            fast = fast.next
            if fast.next:
                fast = fast.next
    return None


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node7 = ListNode(7)
    listHead = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node7
    print(entry_node_of_loop(listHead).value)
