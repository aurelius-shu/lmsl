#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-20
17. 合并链表

测试用例：
功能测试：输入两个含一个或多个结点的链表
异常输入测试：输入一个或两个空链表
'''


from LinkList import ListNode


def merge(listHead1, listHead2):
    if listHead1 == None:
        return listHead2
    if listHead2 == None:
        return listHead1

    mergeList = None

    if int(listHead1.value) <= int(listHead2.value):
        mergeList = listHead1
        listHead1 = listHead1.next
        mergeList.next = merge(listHead1, listHead2)
    else:
        mergeList = listHead2
        listHead2 = listHead2.next
        mergeList.next = merge(listHead1, listHead2)

    return mergeList


if __name__ == '__main__':
    listHead1 = ListNode('1')
    curNode = listHead1
    for i in range(10):
        if (i+1) & 1 == 1:
            curNode.next = ListNode(str(i+1))
            curNode = curNode.next

    listHead2 = ListNode('0')
    curNode = listHead2
    for i in range(10):
        if (i+1) & 1 == 0:
            curNode.next = ListNode(str(i+1))
            curNode = curNode.next
    # listHead2 = None

    print(listHead1)
    print(listHead2)
    mergeList = merge(listHead1, listHead2)
    print(mergeList)
