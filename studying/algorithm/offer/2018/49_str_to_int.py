#!/usr/bin/env python3
# -*- coding:utf-8 -*-


'''
49. 把字符串转换成整数

指针是否为空指针以及字符串是否为空字符串；
字符串对于正负号的处理；
输入值是否为合法值，即小于等于'9'，大于等于'0'；
int为32位，需要判断是否溢出；
使用错误标志，区分合法值0和非法值0。
'''


def strtoint(s):
    length = len(s)
    if length == 0:
        return 0
    else:
        minus = False
        hasflag = False
        if s[0] == '-':
            minus = True
            hasflag = True
        if s[0] == '+':
            hasflag = True
        begin = 0
        if hasflag:
            begin = 1
        minus = -1 if minus else 1
        num = 0
        for c in s[begin:]:
            if c >= '0' and c <= '9':
                num = num*10 + minus * (ord(c)-ord('0'))
            else:
                num = 0
                break
        return num


if __name__ == '__main__':
    print(strtoint('+13322'))
