# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        res = {}
        for c in s:
            res[ord(c)] = res.get(ord(c), 0) + 1
        for i in range(len(s)):
            if res[ord(s[i])] == 1:
                return i
        return -1
