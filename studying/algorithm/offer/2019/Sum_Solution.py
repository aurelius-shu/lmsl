# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        # write code here
        fun = {False: lambda x: 0, True: self.Sum_Solution}
        return fun[not not n](n - 1) + n
