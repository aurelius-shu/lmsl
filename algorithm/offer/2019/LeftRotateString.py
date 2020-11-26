# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if not s:
            return ''
        n = n % len(s)
        self._l = [e for e in s]
        start, mid, end = 0, n - 1, len(s) - 1
        self.reverse(start, mid)
        self.reverse(mid + 1, end)
        self.reverse(start, end)
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
