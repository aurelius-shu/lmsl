#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def test():
    n = 2
    printNNumber(n)


def printNNumber(n):
    if n <= 0:
        return

    number = []
    for i in range(0, n):
        number.append('0')

    for i in range(0, 10):
        number[0] = chr(i + ord('0'))
        printNNumberFrom(number, n, 0)


def printNNumberFrom(number, n, index):
    if index == (n - 1):
        printNumber(number, n)
        return

    for i in range(0, 10):
        number[index] = chr(i + ord('0'))
        printNNumberFrom(number, n, index + 1)


def printNumber(number, n):
    isBegin0 = True
    for i in range(0, n):
        if (isBegin0 and number[i] != '0'):
            isBegin0 = False
        if ((isBegin0 == False) or (i == n-1)):
            print('%c' % number[i])
    print("\t")


if __name__ == '__main__':
    test()
