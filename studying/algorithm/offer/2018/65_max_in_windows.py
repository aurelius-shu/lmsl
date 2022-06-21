#!/usr/bin/env python3
# -*- coding:utf-8 -*-


'''
65. 滑动窗口的最大值

使用一个deque存放最大值或可能成为最大值的下标
窗口每移动一位，取当前deque的首位为窗口的最大值，存入maxs数组
'''


from collections import deque


def max_in_windows(numbers, size):
    maxs = []
    # 数组大小必须大于等于窗口大小，窗口大小必须大于0
    if len(numbers) >= size and size >= 1:
        # 只存最大值或可能成为最大值的下标
        index = deque()
        for i in range(size):
            # 若index非空，且新添加的数字大于等于队列中最小的数字，则删除队列中最小的数字
            while index and numbers[i] >= numbers[index[-1]]:
                index.pop()
            index.append(i)
        for i in range(size, len(numbers)):
            maxs.append(numbers[index[0]])
            # 若index非空，且新添加的数字大于等于队列中最小的数字，则删除队列中最小的数字
            while index and numbers[i] >= numbers[index[-1]]:
                index.pop()
            # 控制窗口大小为size
            if index and index[0] <= int(i-size):
                index.popleft()
            index.append(i)
        maxs.append(numbers[index[0]])
    return maxs


if __name__ == '__main__':
    numbers = [2, 3, 4, 2, 6, 2, 5, 1]
    print(numbers)
    print(max_in_windows(numbers, 3))
