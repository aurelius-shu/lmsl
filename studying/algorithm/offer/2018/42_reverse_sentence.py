#!/usr/bin/env python3
# -*- coding:utf-8 -*-


'''
42. 翻转单词顺序 VS 左旋转字符串
'''


# 左旋转字符串
def reverse_sentence(s):
    s_list = s.split(' ')
    return ' '.join(s_list[::-1])


# 左旋转字符串
def LeftRotateString(s, n):
    length = len(s)
    if n <= 0 or length == 0:
        return s
    if n > length:
        n = n % length

    return s[n:]+s[:n]


if __name__ == '__main__':
    # 翻转单词顺序
    s = 'I am a student.'
    rs = reverse_sentence(s)
    print(rs)

    # 左旋转字符串
    s = 'abcdefg'
    rs = LeftRotateString(s, 2)
    print(rs)
