#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-13
stack实现
'''


class Stack(object):
    # 初始化栈为空列表
    def __init__(self):
        self._items = []

    def __str__(self):
        return self._items

    __repr__ = __str__

    # 判断栈是否为空，返回布尔值
    def is_empty(self):
        return self._items == []

    # 返回栈顶元素
    def peek(self):
        return self._items[len(self._items) - 1]

    # 返回栈的大小
    def size(self):
        return len(self._items)

    # 把新的元素堆进栈里面（程序员喜欢把这个过程叫做压栈，入栈，进栈……）
    def push(self, item):
        self._items.append(item)

    # 把栈顶元素丢出去（程序员喜欢把这个过程叫做出栈……）
    def pop(self):
        return self._items.pop()


class SortStack(Stack):

    def __init__(self, sort='asc'):
        super(SortStack, self).__init__()
        self._sort = sort

    def __str__(self):
        return ','.join(map(str, self._items))

    __repr__ = __str__

    def push(self, item):
        if len(self._items) == 0:
            self._items.append(item)
        else:
            index = self.quick_find(item, 0, len(self._items)-1)
            self._items.insert(index, item)

    def quick_find(self, item, start, end):
        # 找到插入的位置
        if start == end:
            # 正序排列时插入的数字比当前位值小 or 倒叙排列时插入的数字比当前位值大，则将该数插入到当前位的前一位
            if (self._sort == 'asc' and item < self._items[start]) or (self._sort == 'desc' and item > self._items[start]):
                return start
            # 否则插入到当前位的后一位
            else:
                return start + 1

        # 排序栈的中间位
        mid_index = (end + start) >> 1
        if item == self._items[mid_index]:
            return mid_index

        # 顺序
        if self._sort == 'asc':
            # 大于中位的排右边
            if item > self._items[mid_index]:
                return self.quick_find(item, mid_index+1, end)
            # 小于中位的排左边
            else:
                return self.quick_find(item, start, mid_index)
        # 逆序
        elif self._sort == 'desc':
            # 大于中位的排左边
            if item > self._items[mid_index]:
                return self.quick_find(item, start, mid_index)
            # 小于中位的排右边
            else:
                return self.quick_find(item, mid_index+1, end)
        else:
            return None


if __name__ == '__main__':
    # # 初始化一个栈对象
    # my_stack = Stack()
    # # 把'h'丢进栈里
    # my_stack.push('h')
    # print('push', 'h')
    # # 把'a'丢进栈里
    # my_stack.push('a')
    # print('push', 'a')
    # # 看一下栈的大小（有几个元素）
    # print('栈的大小:', my_stack.size())
    # # 打印栈顶元素
    # print('栈顶元素:', my_stack.peek())
    # # 把栈顶元素丢出去，并打印出来
    # print('弹出栈顶，并打印:', my_stack.pop())
    # # 再看一下栈顶元素是谁
    # print('栈顶元素:', my_stack.peek())
    # # 这个时候栈的大小是多少？
    # print('栈的大小:', my_stack.size())
    # # 再丢一个栈顶元素
    # print('再弹一个栈顶:', my_stack.pop())
    # # 看一下栈的大小
    # print('栈的大小:', my_stack.size())
    # # 栈是不是空了？
    # print('栈是否空:', my_stack.is_empty())
    # # 结束
    # print('结束')

    sortStack1 = SortStack()
    sortStack2 = SortStack('desc')
    sortStack1.push(3)
    sortStack1.push(1)
    sortStack1.push(2)
    sortStack1.push(5)
    sortStack1.push(4)

    sortStack2.push(3)
    sortStack2.push(1)
    sortStack2.push(2)
    sortStack2.push(5)
    sortStack2.push(4)

    print(sortStack1)
    print(sortStack2)
