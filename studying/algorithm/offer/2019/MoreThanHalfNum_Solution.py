# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        result = numbers[0]
        times = 1
        for i in range(1, len(numbers)):
            times = times + 1 if numbers[i] == result else times - 1
            if times == 0:
                result = numbers[i]
                times = 1
        times = 0
        for i in range(len(numbers)):
            if numbers[i] == result:
                times += 1
        return result if times > len(numbers) // 2 else 0
