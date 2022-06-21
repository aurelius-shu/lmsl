#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-15
15. 链表中倒数第n个结点

测试用例：
功能测试：输入一个或多个结点的链表和小于链表长度的n
边界输入测试：输入一个或多个结点的链表和等于链表长度的n
异常输入测试：输入一个或多个结点的链表和大于链表长度的n， 输入空链表
'''


from LinkList import ListNode


def find_nth_totail(listHead, n):
    if listHead == None or n < 1:
        raise Exception('Involid input')

    pahead = listHead
    pbehind = listHead

    for i in range(n-1):
        if pahead.next is None:
            raise Exception('超过链表长度(%s)' % (i+1))
        else:
            pahead = pahead.next

    while pahead.next is not None:
        pahead = pahead.next
        pbehind = pbehind.next

    print(pbehind.value)


if __name__ == '__main__':
    linkHead = ListNode('0')
    curNode = linkHead
    for i in range(10):
        curNode.next = ListNode(str(i+1))
        curNode = curNode.next

    find_nth_totail(linkHead, 110)
