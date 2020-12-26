#-*- coding:utf-8 -*-
"""
题目：
    15. 二进制中1的个数
    请实现一个函数，输入一个整数（以二进制串形式），输出该数二进制表示中 1 的个数。例如，把 9 表示成二进制是 1001，有 2 位是 1。因此，如果输入 9，则该函数输出 2。

思路：
（位运算）
判定最右位是否为 1 的方法是与 1 做与运算
数字二进制向右位移: >>

注意：
负数的二进制表示是 补码
无法处理负数
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n != 0:
            if n & 1 == 1:
                res += 1
            n = n >> 1
        return res


s = Solution()
res = s.hammingWeight(9)
print(res)