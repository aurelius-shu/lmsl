# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if not num or size < 1 or len(num) < size:
            return []
        win = num[:size]
        res = [max(win)]
        while size < len(num):
            size += 1
            win.pop(0)
            win.append(num[size - 1])
            res.append(max(win))
        return res
