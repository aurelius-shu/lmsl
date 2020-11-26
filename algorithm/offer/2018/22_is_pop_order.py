#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-21
22. 栈的压入、弹出序列


测试用例：
1、功能测试：输入的两个数组有一个或多个数字，输入的第二个序列是第一个序列所表示的压入序列的栈的弹出序列
2、特殊输入测试（输入两个none）
'''


from stack import Stack


def is_pop_order(list1, list2):
    ispoporder = False
    if list1 != None and list2 != None and len(list1) == len(list2):
        length = len(list1)
        index1 = 0
        index2 = 0
        stack = Stack()
        while length > index2:
            while stack.is_empty() or stack.peek() != list2[index2]:
                if length == index1:
                    break
                stack.push(list1[index1])
                index1 += 1

            if stack.peek() != list2[index2]:
                break

            stack.pop()
            index2 += 1

        if stack.is_empty() and length == index2:
            ispoporder = True

    return ispoporder


if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 3, 2, 1]

    print(is_pop_order(list1, list2))
