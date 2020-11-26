#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-12
快速排序

分治法（D&C策略)：
    1、找出基线条件，这个条件必须尽量简单
    2、不断将问题分解，缩小问题规模，直至符合基线条件

D&C算法是递归的
'''


def quick_sort(arr):
    if(len(arr) < 2):
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    print(quick_sort([10, 2, 6, 5, 9]))
