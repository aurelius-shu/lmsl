# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self._list = []

    def push(self, item):
        if not self._list:
            self._list.append(item)
        else:
            index = self.findIndex(item, 0, len(self._list) - 1)
            self._list.insert(index, item)
            if len(self._list) > self._k:
                self._list.pop()

    def findIndex(self, item, start, end):
        if start >= end:
            if item < self._list[start]:
                return start
            else:
                return start + 1
        mid = (start + end) >> 1
        if item == self._list[mid]:
            return mid
        elif item < self._list[mid]:
            return self.findIndex(item, start, mid - 1)
        else:
            return self.findIndex(item, mid + 1, end)

    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k < 1 or not tinput or k > len(tinput):
            return self._list

        self._k = k
        for x in tinput:
            self.push(x)
        return self._list
