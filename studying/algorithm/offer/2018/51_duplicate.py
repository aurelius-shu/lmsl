#!/usr/bin/env python3
# -*- coding:utf-8 -*-


'''
51. 数组中重复的数字

1. 排序后遍历（O(nlogn）
2. hash表存储数字出现的次数（O(n)）+（O(n)）
3. 判断当前为位的值与下标是否相等：（O(n)）+（O(1)）
    相等，则遍历下一位
    不等，则将当前位i上的元素与a[i]上的元素比较，若他们相等，则找到第一个相同的元素，若不等，则交换它们，换完之后a[i]位置上的值和它的下标是对应的，但i位置上的元素和下标并不一定对应；
    重复2的操作，直到当前位置i的值也为i，将i向后移一位，再重复2。
'''


def duplicate2(numbers):
    if len(numbers) == 0:
        return False

    s = []
    for number in numbers:
        if number in s:
            return True, number
        else:
            s.append(number)
    return False, None


def duplicate3(numbers):
    if not numbers or len(numbers) <= 0:
        return False, None

    length = len(numbers)
    for number in numbers:
        if number < 0 or number > length-1:
            return False, None

    for i in range(len(numbers)):
        # 如果i 与 i位的值不相等
        while(numbers[i] != i):
            # 如果i位的值作为索引号，与该索引对应的值相等
            if numbers[numbers[i]] == numbers[i]:
                return True, numbers[i]
            else:
                tmp = numbers[i]
                tmpi = numbers[i]
                numbers[i] = numbers[numbers[i]]
                numbers[tmpi] = tmp
    return False, None


if __name__ == '__main__':
    print(duplicate2([2, 3, 1, 0, 2, 5, 3]))
    print(duplicate3([2, 3, 1, 0, 2, 5, 3]))
