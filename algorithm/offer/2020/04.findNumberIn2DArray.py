#-*- coding:utf-8 -*-
"""
    04. 二维数组中的查找

    在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

示例:
    现有矩阵 matrix 如下：
    [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    给定 target = 5，返回 true。
    给定 target = 20，返回 false。

限制：
    0 <= n <= 1000
    0 <= m <= 1000

思路：
    从矩阵的左下角或右上角开始遍历，比当前树大则向右（下），否则向上（左）
"""


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]],
                            target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        row_nums = len(matrix)
        col_nums = len(matrix[0])
        row, col = row_nums - 1, 0
        while row >= 0 and col < col_nums:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                row -= 1
            else:
                col += 1

        return False