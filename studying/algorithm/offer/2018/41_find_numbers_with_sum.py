#!/usr/bin/env python3
# -*- coding:utf-8 -*-


'''
41. 和为s的两个数字 VS 何为s的连续正数序列
'''

# 和为s的两个数字
def find_numbers_with_sum(array, sum):
    if len(array) <= 1:
        return []

    left, right = 0, len(array)-1
    while left < right:
        if array[left]+array[right] == sum:
            return array[left], array[right]
        elif array[left]+array[right] >= sum:
            right -= 1
        else:
            left += 1
    return []


# 何为s的连续正数序列
def find_continuous_sequence(sum):
    result = []
    low, high = 1, 2
    while low < high:
        cursum = (low+high) * (high-low+1)/2
        if cursum == sum:
            tmp = []
            for i in range(low, high+1):
                tmp.append(i)
            result.append(tmp)
            low += 1
        elif cursum > sum:
            low += 1
        else:
            high += 1
    return result


if __name__ == '__main__':
    # # 和为s的两个数字
    # array = [1, 3, 5, 6, 7]
    # sum = 11
    # result = find_numbers_with_sum(array, sum)
    # print(result)

    # 何为s的连续正数序列
    result = find_continuous_sequence(100)
    print(result)
