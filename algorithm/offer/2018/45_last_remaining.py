#!/usr/bin/env python3
# -*- coding:utf-8 -*-


'''
45. 圆圈中最后剩下的数字


递推公式：
f[1]=0;
f[i]=(f[i-1]+m)%i; (i>1)
'''


def last_remaining(n, m):
    if n < 1 or m < 1:
        return -1
    last = 0
    for i in range(2, n+1):
        last = (last+m) % i
    return last


if __name__ == '__main__':
    print(last_remaining(5, 3))
