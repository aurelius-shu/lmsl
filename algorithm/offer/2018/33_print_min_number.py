#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-26
33. 把数组排成最小到数

测试用例：
功能测试：输入的数值中有多个数字（有重复数字），输入的数组中只有一个数字
异常输入测试：输入的数组为空
'''


def print_min_number(List):
    if not List:
        return
    strlist = [str(item) for item in List]
    result = quick_sort(strlist)
    return ''.join(result)


def compare_str(str1, str2):
    rstr1 = str1+str2
    rstr2 = str2+str1

    return rstr1 > rstr2


def quick_sort(arr):
    if(len(arr) < 2):
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if not compare_str(i, pivot)]
        greater = [i for i in arr[1:] if compare_str(i, pivot)]
        return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    # a = '55555'
    # b = '124'
    # print(compare_str(a, b))

    # List = [3, 32, 321, 1]
    List = []
    print(print_min_number(List))
