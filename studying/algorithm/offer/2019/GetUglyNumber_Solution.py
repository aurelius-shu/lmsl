# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index<1:
            return 0
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        for i in range(1, index+1):
            next2, next3, next5 = ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5
            ugly.append(min(next2, next3, next5))
            if ugly[i] == next2:
                i2 += 1
            if ugly[i] == next3:
                i3 += 1
            if ugly[i] == next5:
                i5 += 1
        return ugly[index - 1]
