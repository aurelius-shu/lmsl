# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self._data = []
        self._min = []

    def push(self, node):
        self._data.append(node)
        if self._min and self._min[-1] < node:
            self._min.append(self._min[-1])
        else:
            self._min.append(node)

    # write code here
    def pop(self):
        if self._data:
            self._min.pop()
            return self._data.pop()
        else:
            raise Exception('empty.')

    # write code here
    def top(self):
        if self._data:
            return self._data[-1]
        else:
            return None

    # write code here
    def min(self):
        if self._min:
            return self._min[-1]
        else:
            return None
