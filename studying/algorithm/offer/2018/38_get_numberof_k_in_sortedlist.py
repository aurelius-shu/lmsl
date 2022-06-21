#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurelius Shu'

'''
2018-08-26
38. 数字在排序数组中出现的次数

测试用例：
功能测试：输入的数组中有／没有要查找的数字，要查找的数字在数组中有多个／一个
边界测试：要查找的数字是数组的最小／最大值，数组只有一个值
性能测试：数组为空
'''


def get_firstk(List, k, start, end):
    if start > end:
        return -1

    mid_index = (start+end)//2
    mid_data = List[mid_index]

    if mid_data == k:
        if mid_index == 0 or List[mid_index-1] < k:
            return mid_index
        else:
            end = mid_index-1
    elif k < mid_data:
        end = mid_index-1
    else:
        start = mid_index+1

    return get_firstk(List, k, start, end)


def get_lastk(List, k, start, end):
    if start > end:
        return -1

    mid_index = (start+end)//2
    mid_data = List[mid_index]

    if mid_data == k:
        if mid_index == len(List)-1 or List[mid_index+1] > k:
            return mid_index
        else:
            start = mid_index+1
    elif k < mid_data:
        end = mid_index-1
    else:
        start = mid_index+1

    return get_lastk(List, k, start, end)


def get_numberof_k_in_sortedlist(List, k):
    if not List:
        raise Exception('input invalid')

    firstkindex = get_firstk(List, k, 0, len(List)-1)
    lastkindex = get_lastk(List, k, 0, len(List)-1)

    if firstkindex > -1 and lastkindex > -1:
        return lastkindex-firstkindex+1
    else:
        return 0


if __name__ == '__main__':
    List = [1, 1, 2, 3, 3, 3, 4, 5, 6]
    print(get_numberof_k_in_sortedlist(List, 0))
