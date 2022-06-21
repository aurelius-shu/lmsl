#!/usr/bin/env python3
# -*- coding:utf-8 -*-


'''
55. 字符流中第一个不重复的字符
'''

from collections import Counter


def first_appearing_once(s):
    sbak = []
    c = Counter()
    for ch in s:
        c[ch] += 1
        sbak.append(ch)

    for ch in sbak:
        if c[ch] == 1:
            return ch
    return '#'


if __name__ == '__main__':
    s = 'googlel'
    print(first_appearing_once(s))
