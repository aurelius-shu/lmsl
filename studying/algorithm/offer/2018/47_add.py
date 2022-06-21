#!/usr/bin/env python3
# -*- coding:utf-8 -*-


'''
47. 不用加减乘除做加法

a+b = a^b + (a&b)<<1
'''


def add(num1, num2):
    # 位限制
    MAX = 0x7fffffff
    mask = 0xffffffff
    while num2 != 0:
        num1, num2 = (num1 ^ num2), ((num1 & num2) << 1)
        num1 &= mask
        num2 &= mask
    return num1 if num1 <= MAX else ~(num1 ^ mask)


if __name__ == '__main__':
    print(add(-1, 6))
