# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return 0
        greatest, sum = array[0], array[0]
        for i in array[1:]:
            if sum <= 0:
                sum = i
            else:
                sum += i
            greatest = max(greatest, sum)
        return greatest
