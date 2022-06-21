#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-25
30. 最小的k个数

测试用例：
功能测试：输入的数组有/没有相同的数字
边界测试：输入的k等于1或者等于数组的长度
异常输入测试：输入的数组为空，或者输入的k小于1，或者输入的k大于数组的长度
'''

from stack import SortStack


def get_least_numbers(List, k):
    if not List or k < 1 or k > len(List):
        raise Exception('input invalid')

    sortstack = SortStack()
    for item in List:
        if sortstack.size() < k:
            sortstack.push(item)
        elif sortstack.peek() > item:
            sortstack.pop()
            sortstack.push(item)

    return sortstack


if __name__ == '__main__':
    List = [1, 4, 3, 2, 1, 5, 9, 8, 7, 6]
    k = 3

    result = get_least_numbers(List, 5)
    print(result)
