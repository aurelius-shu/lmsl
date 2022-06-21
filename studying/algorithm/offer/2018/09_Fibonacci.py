#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-14
9. 斐波那契数列

循环法

测试用例：
功能测试：输入3，5，10等
边界输入测试：0，1，2
性能测试：100
'''


def Fibonacci(n):
    if n < 1:
        return []
    if n < 2:
        return [1]

    one = 1
    two = 1
    fibN = 0
    fib = [1, 1]
    for i in range(n-2):
        fib.append(one+two)
        fibN = one + two
        one = two
        two = fibN

    return fib


if __name__ == '__main__':
    print(Fibonacci(101))
