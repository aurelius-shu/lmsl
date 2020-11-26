#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-23
28. 字符串的全排列

测试用例：
功能测试：输入的字符串有一个或多个字符
异常输入测试：输入none或空字符串
'''


def string_permutation(string, index):
    if string == None:
        return

    if len(string) == index+1:
        print(string)

    for i in range(len(string)-index):
        temp = string[index+i]
        string[index+i] = string[index]
        string[index] = temp

        string_permutation(string, index+1)

        temp = string[index+i]
        string[index+i] = string[index]
        string[index] = temp


if __name__ == '__main__':
    string = [1, 2, 3, 4, 5]
    # string = []
    string_permutation(string, 0)
