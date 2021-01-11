#-*- coding:utf-8 -*-
"""
题目：
    14-1. 剪绳子
    给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

思路：
    f(2) = 1
    f(3) = max(max(1*2, 1*f(2)), max(2*1, 2*f(1)))
    f(4) = max(max(1*3, 1*f(3)), max(2*2, 2*f(2)), max(3*1, 3*f(1)))
    ......
    f(n) = max(max(1*(n-1), 1*f(n-1)), max(2*(n-2), 2*f(n-2)), ..., max((n-1)*1, (n-1)*f(1)))
"""


class Solution:
    def __init__(self):
        self.d = {2: 1}

    def cuttingRope(self, n: int) -> int:

        if n <= 2:
            return 1

        # items = [max(i * (n - i), i * self.cuttingRope(n - i)) for i in range(1, n)]
        items = []
        for i in range(1, n):
            if n - i not in self.d:
                self.d[n - i] = self.cuttingRope(n - i)
            items.append(max(i * (n - i), i * self.d[n - i]))
        return max(items)
