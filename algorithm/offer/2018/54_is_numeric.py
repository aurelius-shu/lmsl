#!/usr/bin/env python3
# -*- coding:utf-8 -*-


'''
54. 表示数值的字符串

[sign]integral-digits[.[fractional-digits]][e|E[sign]exponential-digits]
'''


def is_numeric(s):
    # 非法输入
    if not s:
        return False

    # 正负号
    if s[0] == '+' or s[0] == '-':
        s = s[1:]

    numeric = True
    s = scanDigits(s)
    if s:
        # 小数判断
        if s[0] == '.':
            s = s[1:]
            s = scanDigits(s)
            # 科学计数法判断
            if s and (s[0] == 'e' or s[0] == 'E'):
                numeric, s = isExponential(s[1:])
        # 无小数，直接科学计数判断
        elif s[0] == 'e' or s[0] == 'E':
            numeric, s = isExponential(s[1:])
        else:
            numeric = False
    return numeric and not s


# 扫描合法的数字
def scanDigits(s):
    while s and ord(s[0]) >= ord('0') and ord(s[0]) <= ord('9'):
        s = s[1:]
    return s


# 判断是否合法的科学计数法尾部
def isExponential(s):
    if s and (s[0] == '+' or s[0] == '-'):
        s = s[1:]
    if not s:
        return False, s
    s = scanDigits(s)
    return not s, s


if __name__ == '__main__':
    s = '3.14'
    print(is_numeric(s))
