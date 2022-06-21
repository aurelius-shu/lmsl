#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-26
34. 丑数(只有2，3，5因子等数)

测试用例：
功能测试：输入3，4，5等
边界测试：输入1，或无效值0
性能测试：较大等数，如10000
'''


def get_ugly_numbers(index):
    if index < 1:
        return 0

    uglynumbers = [1]
    nextuglyindex = 1

    ugly2 = 0
    ugly3 = 0
    ugly5 = 0

    while nextuglyindex < index:
        nextugly = min(uglynumbers[ugly2]*2,
                       uglynumbers[ugly3]*3, uglynumbers[ugly5]*5)
        uglynumbers.append(nextugly)

        while uglynumbers[ugly2] * 2 <= uglynumbers[nextuglyindex]:
            ugly2 += 1
        while uglynumbers[ugly3] * 3 <= uglynumbers[nextuglyindex]:
            ugly3 += 1
        while uglynumbers[ugly5] * 5 <= uglynumbers[nextuglyindex]:
            ugly5 += 1

        nextuglyindex += 1

    ugly = uglynumbers[-1:][0]
    return ugly


if __name__ =='__main__':
    print(get_ugly_numbers(100))