#-*- coding:utf-8 -*-
"""
题目：
    16. 数值的整数次方
    实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。

思路：
    用一个字段记录已经计算出结果的<表达式, 值>
"""


class Solution:
    def __init__(self):
        self.d = {}

    def myPow(self, x, n):
        if 0 == x:
            return 0

        if 0 == n:
            return 1

        if 1 == n:
            return x

        reverse = False
        if n < 0:
            reverse = True
            n = 0 - n
        if (x, n // 2) not in self.d:
            self.d[(x, n // 2)] = self.myPow(x, n // 2)
        if (x, n - (n // 2)) not in self.d:
            self.d[(x, n - (n // 2))] = self.myPow(x, n - (n // 2))
        res = self.d[(x, n // 2)] * self.d[(x, n - (n // 2))]

        if reverse:
            res = 1 / res

        self.d[(x, n)] = res

        return res


s = Solution()
# res = s.myPow(0.00001, 2147483647)
res = s.myPow(2.0000, 10)
print(res)