#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-26
36. 数组中的逆序对

归并排序法

测试用例：
功能测试：输入未排序的数组，输入递增／递减数组，输入含重复数字的数组
边界测试：输入只包涵1个／2个数字的数组
异常输入测试：输入空数组
'''


def inverse_pairs(array):
    if not array:
        return 0

    copyarray = [i for i in array]
    count = inverse_pairs_core(copyarray, array, 0, len(array)-1)
    return count


def inverse_pairs_core(copyarray, array, start, end):
    if start == end:
        copyarray[start] = array[start]
        return 0

    length = (end-start)//2
    left = inverse_pairs_core(copyarray, array, start, start+length)
    right = inverse_pairs_core(copyarray, array, start+length+1, end)

    count = 0
    leftlast = start+length
    rightlast = end
    copyindex = end

    while leftlast >= start and rightlast >= start+length+1:
        if copyarray[leftlast] > copyarray[rightlast]:
            count += rightlast-start-length
            print('本轮逆序对数：',rightlast-start-length)
            for i in range(rightlast-start-length):
                print(copyarray[leftlast], copyarray[rightlast-i])
            print('--')
            copyarray[copyindex] = array[leftlast]
            copyindex -= 1
            leftlast -= 1
        else:
            copyarray[copyindex] = array[rightlast]
            copyindex -= 1
            rightlast -= 1

    while leftlast >= start:
        copyarray[copyindex] = array[leftlast]
        copyindex -= 1
        leftlast -= 1

    while rightlast >= start+length+1:
        copyarray[copyindex] = array[rightlast]
        copyindex -= 1
        rightlast -= 1

    return left + count + right


if __name__ == '__main__':
    array = [7, 5, 6, 4]
    print('总逆序对数：',inverse_pairs(array))
