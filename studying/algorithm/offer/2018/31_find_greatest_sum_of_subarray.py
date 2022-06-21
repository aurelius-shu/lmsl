#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-25
31. 连续子数组的最大和

测试用例：
功能测试：输入的数组有正有负／只有正／只有负
异常输入测试：输入的数组为空
'''


def find_greatestsum_of_subarray(List):
    if not List:
        return

    cursum = 0
    greatestsum = 0

    for item in List:
        if cursum < 0:
            cursum = item
        else:
            cursum += item

        if cursum > greatestsum:
            greatestsum = cursum

    return greatestsum


if __name__ == '__main__':
    # List = [1, -2, 3, 10, -4, 7, 2, -5]
    # List = [-3, -1, -2, -5]
    List = [5, 1, 2, 3]
    print(find_greatestsum_of_subarray(List))
