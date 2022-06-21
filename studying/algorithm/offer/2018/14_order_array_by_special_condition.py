#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-15
14. 数值排序，将符合条件的放在前部，不符合条件的放在后部

测试用例：
功能测试：输入奇偶交替的数值数组，输入奇数都在偶数前面的数组，输入偶数都在奇数前面的数组（含负数和0）
特殊输入测试：数组为空
'''


# 满足的条件：eg：是一个偶数
def special_condition(item):
    if isinstance(item, int) and item & 1 == 0:
        return True
    return False


def reorder(array, func):
    if not isinstance(array, list):
        raise Exception('Involid input')
    if len(array) < 1:
        print([])
        return

    start = 0
    end = len(array)-1

    while start < end:
        while start < end and func(array[start]):
            start += 1
        while start < end and not func(array[end]):
            end -= 1

        if start < end:
            temp = array[start]
            array[start] = array[end]
            array[end] = temp

    print(array)


if __name__ == '__main__':
    array = [0, 1, 3, 5, 7, 2, 6, -2]
    # array = []
    reorder(array, special_condition)
 