#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-26
40. 数组中只出现一次的两个数（其他都出现两次）

确定数组中有且只有两个出现一次的数，且其他数都出现来双数次

测试用例：
功能测试：数组中有／没有多对重复都数字，数字中有两个只出现一次都数，数组中只有一个／没有只出现一次都数
异常输入测试：数组为空
'''


def find_numbers_appear_once(List):
    if List == None:
        return None, None

    exclusiveor = 0
    for i in List:
        exclusiveor ^= i

    indexofbit1 = find_first_bit_1(exclusiveor)

    num1, num2 = 0, 0
    for i in List:
        if is_bit1(i, indexofbit1):
            num1 ^= i
        else:
            num2 ^= i
    return num1, num2


def is_bit1(number, index):
    number = number >> index
    return number & 1 == 1


def find_first_bit_1(number):
    if not isinstance(number, int):
        raise Exception('number must be a int type object')

    index = 0
    while number & 1 != 1 and number != 0:
        number = number >> 1
        index += 1

    if number & 1 == 1:
        return index
    else:
        raise Exception('not found bit_1')


if __name__ == '__main__':
    List = [121, 23, 23, 421, 33, 33]
    # List = None
    print(find_numbers_appear_once(List))
