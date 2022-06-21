#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-15
16. 反转链表

测试用例：
功能测试：输入一个或多个结点的链表
异常输入测试：输入空链表
'''


from LinkList import ListNode


def reverse_linklist(listHead):
    if listHead == None:
        return None
    if listHead.next == None:
        return listHead

    preNode = None
    curNode = listHead
    nextNode = curNode.next
    while nextNode != None:
        curNode.next = preNode
        preNode = curNode
        curNode = nextNode
        nextNode = curNode.next
    curNode.next = preNode
    return curNode


if __name__ == '__main__':
    listHead_1 = ListNode('0')
    curNode = listHead_1
    for i in range(9):
        curNode.next = ListNode(str(i+1))
        curNode = curNode.next

    listHead_2 = ListNode('0')

    listHead_3 = None
    # print(listHead_1)
    print(reverse_linklist(listHead_1))
