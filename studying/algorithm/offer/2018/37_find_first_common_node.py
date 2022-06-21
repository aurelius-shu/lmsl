#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-26
37. 两个链表的第一个公共界点

测试用例：
功能测试：两个链表存在／不存在公共结点
边界测试：第一个公共界点在开头／结尾
异常输入测试：字符串为空
'''


from LinkList import ListNode


def find_first_common_node(list1, list2):
    if not list1 or not list2:
        return

    size1 = get_listsize(list1)
    size2 = get_listsize(list2)
    difsize = size1-size2

    longlist = list1
    shortlist = list2
    if size1 < size2:
        longlist = list2
        shortlist = list1

    while difsize > 0 and longlist.next != None:
        longlist = longlist.next
        difsize -= 1

    while longlist.next != None and shortlist.next != None and longlist.value != shortlist.value:
        longlist = longlist.next
        shortlist = shortlist.next

    if longlist.vlaue == shortlist.value:
        return longlist

    return None


def get_listsize(listNode):
    if listNode == None:
        return 0

    size = 1
    while listNode.next != None:
        listNode = listNode.next
        size += 1

    return size


if __name__ == '__main__':
    list1 = ListNode(1)
    list2 = ListNode(2)

    node11 = ListNode(11)
    node12 = ListNode(12)
    node13 = ListNode(13)

    list1.next = node11
    node11.next = node12
    node12.next = node13

    node21 = ListNode(21)
    node22 = ListNode(22)
    list2.next = node21
    node21.next = node22

    commonnode1 = ListNode(3)
    commonnode2 = ListNode(4)

    node13.next = commonnode1
    node22.next = commonnode1
    # commonnode1.next = commonnode2

    commonnode = find_first_common_node(list1, list2)

    print(commonnode)
