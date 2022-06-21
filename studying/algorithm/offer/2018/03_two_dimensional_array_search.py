#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-13
3. 二维数组中的查找

测试用例：
1、最大值，最小值，区间内值
2、查找数组中没有的数
3、特殊输入（空指针，空数组）
'''


def find(td_array, number):
    result = [False]

    if td_array is not None and len(td_array) > 0:
        total_row = len(td_array)
        row = 0
        column = len(td_array[0])-1
        while(row < total_row and column >= 0):
            if td_array[row][column] == number:
                result[0] = True
                result += [row, column]
                break
            elif td_array[row][column] > number:
                column -= 1
            else:
                row += 1

    return result


if __name__ == '__main__':
    td_array = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    # td_array = [[]]
    number = 7
    print(find(td_array, number))
