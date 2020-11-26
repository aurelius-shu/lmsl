#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-13
5. 从尾到头打印链表

方案1. 栈
方案2. 递归

测试用例：
1、功能测试（输入到链表有多个节点，输入到链表只有一个节点）
2、特殊输入测试（输入到链表指向null）
'''


from stack import Stack


# 栈 实现 倒序打印
def stack_inverted_order_print(List, start):

    stack = Stack()
    stack.push(start)

    node = List[start]
    while node:
        stack.push(node)
        node = List[node] if node in List else None

    while stack.size():
        print(stack.pop())


# 递归 实现 倒序打印
def recursion_inverted_order_print(List, start):
    if start not in List:
        return None
    elif List[start]:
        recursion_inverted_order_print(List, List[start])
    print(start)


if __name__ == '__main__':
    List = {}
    List['start'] = 'a'
    List['a'] = 'b'
    List['b'] = 'c'
    List['c'] = 'd'
    List['d'] = {}

    # List['start'] = 'a'
    # List['a'] = {}

    start = 'start'

    stack_inverted_order_print(List, start)
    # recursion_inverted_order_print(List, start)
