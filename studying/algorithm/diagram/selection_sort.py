#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-12
选择排序
        数组    链表
读取    O(1)    O(n)
插入    O(n)    O(1)
删除    O(n)    O(1)
'''


def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i, val in enumerate(arr):
        if smallest > val:
            smallest = val
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


if __name__ == '__main__':
    print(selection_sort([5, 3, 6, 2, 10]))
