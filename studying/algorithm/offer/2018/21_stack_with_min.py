#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-21
21. 包含min函数的栈

测试用例：
压入的值比之前的最小值大／小
弹出大值是／不是最小值
'''


from stack import Stack


class StackWithMin(object):

    def __init__(self):
        self._data = Stack()
        self._min = Stack()

    def push(self, value):
        self._data.push(value)
        if self._min.size() == 0 or value < self._min.peek():
            self._min.push(value)
        else:
            self._min.push(self._min.peek())

    def pop(self):
        assert self._data.size() > 0 and self._min.size() > 0, '空栈不可执行pop操作'
        self._data.pop()
        self._min.pop()

    def min(self):
        assert self._data.size() > 0 and self._min.size() > 0, '空栈不可执行min操作'
        return self._min.peek()


if __name__ == '__main__':
    stack = StackWithMin()
    stack.push(5)
    print('push: 5')
    print('min:',stack.min())

    stack.push(4)
    print('push: 4')
    print('min:',stack.min())

    stack.push(6)
    print('push: 6')
    print('min:',stack.min())

    stack.pop()
    print('pop')
    print('min:',stack.min())

    stack.pop()
    print('pop')
    print('min:',stack.min())

    stack.pop()
    print('pop')
    print('min:',stack.min())

    