#!/usr/bin/env python3
# -*- coding:utf-8 -*-


'''
52. 构建乘积数组

1. reduce 直接计算
2. 可以把B[i]=A[0]*A[1]*.....*A[i-1]*A[i+1]*.....*A[n-1]。看成A[0]*A[1]*.....*A[i-1]和A[i+1]*.....A[n-2]*A[n-1]两部分的乘积
'''

from functools import reduce


def multiply1(A):
    B = []
    if len(A) == 0:
        return B
    else:
        for i in range(len(A)):
            tmp = A[i]
            A[i] = 1
            B.append(reduce(lambda x, y: x*y, A))
            A[i] = tmp
    return B


def multiply2(A):
    length = len(A)
    B = [0 for i in range(length)]
    if length <= 0:
        return B

    B[0] = 1
    # 左边
    for i in range(1, length):
        B[i] = B[i-1] * A[i-1]

    # 右边
    temp = 1
    for i in range(length-2, -1, -1):
        temp *= A[i+1]
        # 结果 = 左边*右边
        B[i] *= temp

    return B


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    print(multiply1(A))
    print(multiply2(A))
