#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-26
32. 从1到n整数中1出现到次数

测试用例：
功能测试：输入常规整数5，10，35，99
边界测试：输入0，1
性能测试：输入999999
'''


def number_of1_between_1andn(n):
    if n < 1:
        # raise Exception('input invalid')
        return 0

    return numberof1(n)


def numberof1(n):
    if n < 1:
        return 0

    first = int(str(n)[:1])
    lenght = len(str(n))

    if lenght == 1 and first == 0:
        return 0
    if lenght == 1 and first > 0:
        return 1

    numberof1infirstcase = 0
    if first == 1:
        numberof1infirstcase = 1+int(str(n)[1:])
    else:
        numberof1infirstcase = pow(10, lenght-1)

    numberof1inothercase = first * (lenght-1) * pow(10, lenght-2)
    numberof1inlower = numberof1(int(str(n)[1:]))

    return numberof1infirstcase + numberof1inothercase + numberof1inlower


if __name__ == '__main__':
    # print('5:', number_of1_between_1andn(5))
    # print('10:', number_of1_between_1andn(10))
    print('35:', number_of1_between_1andn(35))
    # print('99:', number_of1_between_1andn(99))
    # print('0:', number_of1_between_1andn(0))
    # print('1:', number_of1_between_1andn(1))
    # print('-1:', number_of1_between_1andn(-1))
    print('21345', number_of1_between_1andn(21345))
    # print('999999:', number_of1_between_1andn(999999))
