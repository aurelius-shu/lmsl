#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-13
4. 替换空格(不用辅助空间)

测试用例：
1、字符串中含空格（头，中，尾）
2、字符串中不含空格
3、特殊输入（空指针，空数组，一个空格，多个空格）
'''


# 替换字符串中的空格
def replace_blank(string):
    if not isinstance(string, list):
        raise ValueError('入参只可是 list')
    if string is None or len(string) < 1:
        return None

    # string = [s for s in string]
    org_length = len(string)
    blank_number = 0
    for s in string:
        if s == ' ':
            blank_number += 1
    new_length = org_length + blank_number * 2
    string += ['' for i in range(blank_number * 2)]
    while org_length > 0:
        if string[org_length-1] == ' ':
            string[new_length-3] = r'%'
            string[new_length-2] = '2'
            string[new_length-1] = '0'
            new_length -= 3
        else:
            string[new_length-1] = string[org_length-1]
            new_length -= 1
        org_length -= 1

    return string


if __name__ == '__main__':
    # string = 'hello world !  '
    string =' '
    string = [s for s in string]
    string = replace_blank(string)
    string = ''.join(string)
    print(string)
