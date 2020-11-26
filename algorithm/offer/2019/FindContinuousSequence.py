# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        res = []
        start, end, csum = 1, 2, 3
        while end < tsum:
            if csum > tsum:
                csum -= start
                start += 1
            elif csum < tsum:
                end += 1
                csum += end
            else:
                res.append(list(range(start, end + 1)))
                csum -= start
                start += 1
                end += 1
                csum += end
        return res
