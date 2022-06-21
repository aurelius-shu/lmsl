#-*- coding:utf-8 -*-
"""
    13. 机器人的运动范围

    地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

示例 1：
    输入：m = 2, n = 3, k = 1
    输出：3

示例 2：
    输入：m = 3, n = 1, k = 0
    输出：1
提示：
    1 <= n,m <= 100
    0 <= k <= 20

思路：
    递归：
        边界条件：
            结束条件：
                1. 超过边界
                2. 已标记走过的节点
                3. 经检查走不进去的节点
        递归处理：向下或向右行走
"""


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        matrix = [[1] * n for i in range(m)]
        res = 0

        def check(i, j):
            nonlocal matrix
            nonlocal res

            if i < 0 or i >= m or j < 0 or j >= n: return
            if matrix[i][j] == 0: return
            if not checkSum(i, j): return

            if matrix[i][j] == 1:
                matrix[i][j] = 0
                res += 1

            check(i + 1, j)
            check(i, j + 1)

        def checkSum(i, j):
            if matrix[i][j] == 0:
                return True

            ij = str(i) + str(j)
            total = 0
            for c in str(ij):
                total += int(c)
            return total <= k

        check(0, 0)
        return res