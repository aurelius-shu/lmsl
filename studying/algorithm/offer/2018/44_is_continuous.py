#!/usr/bin/env python3
# -*- coding:utf-8 -*-


'''
44. 扑克牌中的顺子

输入数据个数为5；
输入数据都在0-13之间；
没有相同的数字；
最大值与最小值的差值不大于5。
'''


def IsContinuous(numbers):
    if len(numbers) < 5:
        return False
    max_num = -1
    min_num = 14
    flag = 0
    for number in numbers:
        # 非法输入
        if number < 0 or number > 13:
            return False
        # 大小王
        if number == 0:
            continue
        # number 已经存在
        if (flag >> number) & 1 == 1:
            return False
        # 位记录数字
        flag |= 1 << number
        if number < min_num:
            min_num = number
        if number > max_num:
            max_num = number
        if max_num-min_num >= 5:
            return False
    return True


if __name__ == '__main__':
    numbers = [0, 2, 4, 7, 5]
    print(IsContinuous(numbers))
