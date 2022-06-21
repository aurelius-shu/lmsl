#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-20
20. 顺时针打印矩阵

测试用例：
数组右多行多列，数组只有一行，数组只有一列，数组只有一行一列
'''


def print_matrix_circly(numbers):
    if numbers == None or len(numbers) <= 0 or len(numbers[0]) <= 0:
        return

    length = len(numbers)
    width = len(numbers[0])

    start = 0
    while start*2 < length and start*2 < width:
        print_matrix_incircle(numbers, start)
        start += 1


def print_matrix_incircle(numbers, start):
    endx = len(numbers[0])-1-start
    endy = len(numbers)-1-start

    nums = []

    # 从左到右
    for i in range(endx+1-start):
        nums.append(numbers[start][start+i])

    # 从上到下
    if start < endx and start < endy:
        for i in range(endy-start):
            nums.append(numbers[start+i+1][endx])

    # 从右到左
    if start < endx and start < endy:
        for i in range(endx-start):
            nums.append(numbers[endy][endx-1-i])

    # 从下到上
    if start < endy-1:
        for i in range(endy-1-start):
            nums.append(numbers[endy-1-i][start])

    print(nums)


if __name__ == '__main__':
    # numbers = [[i for i in range(10)] for j in range(10)]
    numbers = [[i for i in range(1)] for j in range(10)]
    print_matrix_circly(numbers)
