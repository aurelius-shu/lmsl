#-*- coding:utf-8 -*-
"""
    剑指 Offer 44. 数字序列中某一位的数字
    数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。

    请写一个函数，求任意第n位对应的数字。

    示例 1：
        输入：n = 3
        输出：3

    示例 2：
        输入：n = 11
        输出：0
    限制：
        0 <= n < 2^31

    思路：
        digit, start, count
        0，1个数，1位
        1 位数，9*1 个数，9位
        2 位数，9*10 个数，9*2*10位
        3 位数，9*100 个数，9*3*100位
        n 位数，9*10**n 个数，9*n*10**n位

        减掉前面完整的位，从start 开始算起，找到数字：start + (n-1)/digit        
"""


class Solution:
    def findNthDigit(self, n: int) -> int:
        start, digit, count = 1, 1, 9
        while n > count:
            n -= count
            start *= 10
            digit += 1
            count = 9 * start * digit
        num = start + (n - 1) / digit
        return int(str(num)[(n - 1) % digit])
