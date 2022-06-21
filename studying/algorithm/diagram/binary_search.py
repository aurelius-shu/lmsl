#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-12
二分查找
'''


def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high)//2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == '__main__':
    _list = [1, 3, 5, 7, 9]
    print(binary_search(_list, 7))
    print(binary_search(_list, -1))
