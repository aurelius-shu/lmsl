#!/usr/bin/env python3
# -*- coding:utf-8 -*-


'''
46. 求1+2+3+...+n

不能用乘除法、for、while、if、else、switch、case等关键字和条件判断语句（A?B:C)
'''


def SumTeminator(n):
    return 0


def Sum(n):
    fun = {False: SumTeminator, True: Sum}
    result = fun[not not n](n-1) + n
    return result


if __name__ == '__main__':
    print(Sum(2))
