#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-24
29. 数组中出现次数超过一半的数字

测试用例：
功能测试：输入的数组中存在/不存在一个出现次数超过一半的数字
异常输入测试：输入的数组为空
'''


def morethanhalfnum(List):
    if not List:
        return None

    result = List[0]
    times = 1
    for i in range(len(List)):
        if times == 0:
            result = List[i]
            times = 1
        elif List[i] == result:
            times += 1
        else:
            times -= 1

    times = 0
    for i in range(len(List)):
        if List[i] == result:
            times += 1

    if times*2 > len(List):
        return True, result
    else:
        return False, None


if __name__ == '__main__':
    List = [1, 2, 3, 4, 2, 2, 2, 2, 1]
    print(morethanhalfnum(List))
