#!/usr/bin/env python3
# -*- coding:utf-8 -*-


'''
64. 数据流中的中位数

堆排序：用一个最大堆和一个最小堆存储数据流，奇数个放入最大堆，偶数个放入最小堆，当放入最大堆的数比最小对中的最大数大时，将该数放入最小堆，并将最小堆的最大数放入最大堆，反正放入最小堆的数放入最大堆
'''

from stack import SortStack


class Solution(object):

    def __init__(self):
        self._max = SortStack('desc')
        self._min = SortStack()
        # self._slist = slist

    def insert(self, num):
        # 已有数据为偶数个，放入最小堆
        if (self._max.size() + self._min.size()) & 1 == 0:
            if self._max.size() > 0 and num > self._max.peek():
                self._max.push(num)
                num = self._max.pop()
            self._min.push(num)
        # 已有数据为奇数个，放入最大堆
        else:
            if self._min.size() > 0 and num < self._min.peek():
                self._min.push(num)
                num = self._max.pop()
            self._max.push(num)

    def get_median(self):
        print(self._max, '\r\n', self._min)

        size = self._min.size() + self._max.size()
        if size == 0:
            return 0

        if (size & 1) == 0:
            return (self._min.peek() + self._max.peek())/2
        else:
            return self._min.peek()


if __name__ == '__main__':
    slist = [1, 3, 5, 6, 7, 8]
    solution = Solution()
    for s in slist:
        solution.insert(s)
    median = solution.get_median()
    print(slist, ':', median)
