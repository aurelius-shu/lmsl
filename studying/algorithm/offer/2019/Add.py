# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self._max = 0x7fffffff
        self._mask = 0xffffffff

    def Add(self, num1, num2):
        # write code here
        while num2 != 0:
            num1, num2 = num1 ^ num2, (num1 & num2) << 1
            num1 &= self._mask
            num2 &= self._mask

        return num1 if num1 < self._max else ~(num1 ^ self._mask)
