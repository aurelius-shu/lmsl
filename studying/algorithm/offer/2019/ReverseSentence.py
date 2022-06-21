# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if not s:
            return ''
        start, end, stop = 0, 0, len(s)
        self._l = [e for e in s]
        while end <= stop:
            if end == stop or self._l[end] == ' ':
                self.reverse(start, end - 1)
                start = end + 1
            end += 1
        self.reverse(0, stop - 1)
        return ''.join(self._l)

    def reverse(self, start, end):
        while start < end:
            self.swap(start, end)
            start += 1
            end -= 1

    def swap(self, i, j):
        tmp = self._l[i]
        self._l[i] = self._l[j]
        self._l[j] = tmp
