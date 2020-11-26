#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-14
8. 旋转数组中的最小值

测试用例：
1、功能测试：输入数组是一个升序数组的选择，数组中有/没有重复数字
2、边界输入测试：输入的数组是一个升序数组，输入的数组只有一个数字
3、特殊输入测试：空数组
'''


def rotate_array_min(List):
    if List is None or len(List) < 1:
        raise Exception('Invalid paramters')

    pointerStart = 0
    pointerEnd = len(List)-1
    pointerMid = 0
    while List[pointerStart] >= List[pointerEnd]:
        if pointerEnd-pointerStart == 1:
            pointerMid = pointerEnd
            break
        pointerMid = (pointerStart+pointerEnd)//2

        # 如果下标为pointerStart,pointerEnd,pointerMid的三个数字相等，则顺序查找
        if List[pointerStart] == List[pointerEnd] and List[pointerMid] == List[pointerStart]:
            return minInOrder(List, pointerStart, pointerEnd)

        if List[pointerMid] >= List[pointerStart]:
            pointerStart = pointerMid
        elif List[pointerMid] <= List[pointerEnd]:
            pointerEnd = pointerMid

    return pointerMid, List[pointerMid]


def minInOrder(List, start, end):
    minValue = List[start]
    while start < end:
        start += 1
        if minValue > List[start]:
            minValue = List[start]

    return start, minValue


if __name__ == '__main__':
    # List = [4, 5, 6, 7, 1, 2]
    List = [4, 1]
    print(rotate_array_min(List))
