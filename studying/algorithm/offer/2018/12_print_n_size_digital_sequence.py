#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-14
12. 打印1到n位最大数字的序列

考虑大数问题，可以用字符串代替数字

递归法

测试用例：
功能测试：输入1，3，5...
特殊输入测试：输入0,-1
'''


def print_number(number):
    numsize = len(number)
    startindex = numsize-1

    for i in range(numsize):
        if number[i] != '0':
            startindex = i
            break
    print(number[startindex:numsize])


def nsize_digitalsequence_print(n):
    if n < 1:
        raise Exception('Involid input')

    for i in range(10):
        number = [str(i)]
        nsize_digitalsequence_print_recursively(number, n, 0)


def nsize_digitalsequence_print_recursively(number, length, index):
    if index == length-1:
        print_number(''.join(number))
        return

    for i in range(10):
        number.append(str(i))
        nsize_digitalsequence_print_recursively(number, length, index+1)
        number.pop()


if __name__ == '__main__':
    # print_number('00011001')
    nsize_digitalsequence_print(1)
