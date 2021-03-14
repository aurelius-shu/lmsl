#-*- coding:utf-8 -*-
"""
    11. 旋转数组的最小数字

    把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：
    输入：[3,4,5,1,2]
    输出：1

示例 2：
    输入：[2,2,2,0,1]
    输出：0

思路：
    1. 中位数小于末尾数：最小数在前半段
    2. 中位数等于末位数，且中位数不等于首位数：最小数在前半段
    2. 中位数大于等于首位数，且中位数大于末位数：最小数在后半段
    3. 中位数等于首位和末位数：不知道最小数在前还是在后
"""


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        if not numbers:
            raise ValueError("input error.")

        if len(numbers) <= 2:
            return min(numbers)

        length = len(numbers)
        mid = (length - 1) // 2

        if (numbers[mid] < numbers[length - 1]) or (
            (numbers[mid] == numbers[length - 1]) and
            (numbers[mid] != numbers[0])):
            return self.minArray(numbers[:mid + 1])

        if ((numbers[mid] > numbers[length - 1])
                and (numbers[mid] >= numbers[0])):
            return self.minArray(numbers[mid + 1:])

        if numbers[mid] == numbers[length - 1] and numbers[mid] == numbers[0]:
            return min(self.minArray(numbers[mid + 1:]),
                       self.minArray(numbers[:mid + 1]))
