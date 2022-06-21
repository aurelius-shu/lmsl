#-*- coding:utf-8 -*-
"""
题目：
    39. 数组中出现次数超过一半的数字
    数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

    你可以假设数组是非空的，并且给定的数组总是存在多数元素。

思路：
摩尔投票法
    判断是否相等，相等+1，不相等-1，小于等于0换数

注意：
如果可能不存在众数，需要在最终统计验证找到的众数是否是众数
"""


class Solution:
    def majorityElement(self, nums) -> int:
        votes = 0
        for i in nums:
            if votes <= 0:
                cur = i
            votes += 1 if i == cur else -1
        votes = 0
        for i in nums:
            if i == cur:
                votes += 1

        return cur if votes * 2 > len(nums) else None
