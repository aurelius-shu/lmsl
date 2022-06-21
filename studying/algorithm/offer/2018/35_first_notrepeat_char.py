#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-26
35. 第一个只出现一次等字符

测试用例：
功能测试：字符串中存在／不存在只出现一次等字符，字符串中全是只出现一次的字符
性能测试：字符串为空
'''


from collections import Counter


def first_not_repeat_char(string):
    if not string:
        return None

    ch = Counter()
    for c in string:
        ch[c] += 1

    for c in string:
        if ch[c] == 1:
            return c

    return None


if __name__ == '__main__':
    string = '11223319'
    print(first_not_repeat_char(string))
