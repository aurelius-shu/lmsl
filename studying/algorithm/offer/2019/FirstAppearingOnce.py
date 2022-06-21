# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        from collections import Counter
        self._c = Counter()
        self._s = []

    # 返回对应char
    def FirstAppearingOnce(self):
        # write code here
        for ch in self._s:
            if self._c[ch] == 1:
                return ch

    def Insert(self, char):
        # write code here
        self._c[char] += 1
        self._s.append(char)
