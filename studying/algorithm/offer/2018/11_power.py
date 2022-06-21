#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-14
11. 数值的整数次方

测试用例：
底数和指数分别设置为正数／负数／0
'''


def power(base, exponent):
    if (base - 0 < 0.00000000001 or 0-base < 0.00000000001) and exponent == 0:
        raise Exception('Involid input')
    elif base == 0:
        return 0
    exp = exponent
    if exponent < 0:
        exp = -exponent
    result = power_core(base, exp)
    if exponent < 1:
        result = 1/result

    return result


def power_core(base, exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base

    result = power_core(base, exponent >> 1)
    result *= result
    if exponent & 1 == 1:
        result *= base

    return result


if __name__ == '__main__':
    print(power(-10, -1))
