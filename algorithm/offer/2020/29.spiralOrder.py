#-*- coding:utf-8 -*-
"""
题目：
    29. 顺时针打印矩阵
    输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
 
    示例 1：

    输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
    输出：[1,2,3,6,9,8,7,4,5]
    示例 2：

    输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    输出：[1,2,3,4,8,12,11,10,9,5,6,7]

    限制：

    0 <= matrix.length <= 100
    0 <= matrix[i].length <= 100

思路：
    按圈数一次计算每个边的运动轨迹
    向右：cycle, cycle -> cols-cycle
    向下：cycle+1 -> rows-cycle, cols-cycle-1
    向左：rows-cycle-1, cols-cycle-2 -> cycle-1
    向上：rows-cycle-2 -> cycle, cycle

停止条件：
    1. 向右和向下时，圈数的两倍必须分别小于行数和列数
    2. 向右和向上时，圈数的两倍必须分别小于函数和列数减1
    3. 移动不能反向

"""


class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []

        res = []
        rows, cols = len(matrix), len(matrix[0])
        cycle = 0
        while cycle * 2 < rows or cycle * 2 < cols:
            if cycle * 2 < rows and cycle * 2 < cols:
                for i in range(cycle, cols - cycle):
                    res.append(matrix[cycle][i])
            if cycle * 2 < cols and cycle * 2 + 1 < rows:
                for i in range(cycle + 1, rows - cycle):
                    res.append(matrix[i][cols - cycle - 1])
            if cycle * 2 < rows - 1 and cycle * 2 < cols - 1:
                for i in range(cols - cycle - 2, cycle - 1, -1):
                    res.append(matrix[rows - cycle - 1][i])
            if cycle * 2 < cols - 1 and cycle * 2 < rows - 2:
                for i in range(rows - cycle - 2, cycle, -1):
                    res.append(matrix[i][cycle])

            cycle += 1
        return res
