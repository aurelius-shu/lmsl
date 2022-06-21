#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-14
7. 用两个栈实现队列

测试用例：
1、向空队列添加删除元素
2、向非空队列添加删除元素
3、连续删除元素直至队列为空
'''


from stack import Stack


class custom_queue():

    def __init__(self):
        self.__stack1 = Stack()
        self.__stack2 = Stack()

    def push(self, item):
        self.__stack1.push(item)

    def pop(self):
        if self.__stack2.size() <= 0:
            while self.__stack1.size() > 0:
                self.__stack2.push(self.__stack1.pop())

        if self.__stack2.size() == 0:
            raise Exception('queue is empty!')

        return self.__stack2.pop()


if __name__ == '__main__':
    cqueue = custom_queue()

    cqueue.push('a')
    print('push','a')
    cqueue.push('a')
    print('push','a')
    cqueue.push('a')
    print('push','a')
    print('pop',cqueue.pop())
    cqueue.push('b')
    print('push','b')
    print('pop',cqueue.pop())
    # print('pop',cqueue.pop())


