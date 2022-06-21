# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if not matrix or not matrix[0]:
            return []

        l, w = len(matrix), len(matrix[0])
        start = 0
        result = []
        while start * 2 < l and start * 2 < w:
            result += self.printMatrixIncircle(matrix, start)
            start += 1

        return result

    def printMatrixIncircle(self, matrix, start):
        endx = len(matrix[0]) - 1 - start
        endy = len(matrix) - 1 - start
        nums = []

        for i in range(endx + 1 - start):
            nums.append(matrix[start][start + i])

        if start <= endx and start < endy:
            for i in range(endy - start):
                nums.append(matrix[start + i + 1][endx])

        if start < endx and start < endy:
            for i in range(endx - start):
                nums.append(matrix[endy][endx - 1 - i])

        if start < endx and start + 1 < endy:
            for i in range(endy - 1 - start):
                nums.append(matrix[endy - 1 - i][start])

        return nums


if __name__ == '__main__':
    s = Solution()
    l = [[1], [2], [3], [4], [5]]
    r = s.printMatrix(l)
    print(r)
