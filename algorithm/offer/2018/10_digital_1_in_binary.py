#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-14
10. 二进制中1的个数

1. 位（右）移法 --负数会死循环
2. 1左移法
3. (n-1)&n法

测试用例：
1、正数：1，999999999999999999999
2、负数：－1，－999999999999999999
3、0
'''


def count_2(n):
    if n < 0:
        n = 0-n
    count = 0
    flag = 1
    while flag and flag <= n:
        if flag & n:
            count += 1
        flag = flag << 1
    return count


def count_3(n):
    if n < 0:
        n = 0-n
    count = 0
    while n:
        count += 1
        n = (n-1) & n
    return count


if __name__ == '__main__':
    # n = 99999999999999955555555555555555
    n = 0
    print(count_2(n))
    print(count_3(n))
