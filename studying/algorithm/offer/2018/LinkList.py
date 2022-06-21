#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-15
链表 模拟
'''


# 普通链表
class ListNode(object):

    def __init__(self, value):
        self._next = None
        self._value = value

    def __str__(self):
        vals = [self._value]
        curNode = self
        while curNode.next is not None:
            curNode = curNode.next
            vals.append(curNode.value)
        return ','.join([str(i) for i in vals])

    __repr__ = __str__

    @property
    def value(self):
        return self._value

    @value.setter
    def vlaue(self, value):
        self._value = value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next


# 双向链表
class DoublyLinkList(ListNode):

    def __init__(self, value):
        super(DoublyLinkList, self).__init__(value)
        self._last = None

    @property
    def last(self):
        return self._last

    @last.setter
    def last(self, last):
        self._last = last


if __name__ == '__main__':
    LinkList = ListNode('va')
    LinkHead = LinkList
    LinkList.next = ListNode('vb')
    LinkList = LinkList.next
    LinkList.next = ListNode('vc')

    curNode = LinkHead
    print(curNode.value)
    while curNode.next:
        curNode = curNode.next
        print(curNode.value)
