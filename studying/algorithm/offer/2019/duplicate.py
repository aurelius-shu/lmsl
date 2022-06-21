# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        self._numbers = numbers
        for i in range(len(numbers)):
            while self._numbers[i] != i:
                if self._numbers[i] == self._numbers[self._numbers[i]]:
                    duplication[0] = self._numbers[i]
                    return True
                self.swap(self._numbers[i], i)
        return False

    def swap(self, i, j):
        tmp = self._numbers[i]
        self._numbers[i] = self._numbers[j]
        self._numbers[j] = tmp
