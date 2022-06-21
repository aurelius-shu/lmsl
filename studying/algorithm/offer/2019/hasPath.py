# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if not matrix or not rows or not cols or len(matrix) != rows * cols or not path:
            return False
        self._matrix = [matrix[i * cols: (i + 1) * cols] for i in range(rows)]
        self._path = path
        self._rows = rows
        self._cols = cols
        self._visited = [[False] * self._cols for i in range(self._rows)]
        for row in range(self._rows):
            for col in range(self._cols):
                if self.hasPathCore(row, col, 0):
                    return True
        return False

    def hasPathCore(self, row, col, index):
        if index == len(self._path):
            return True
        res = False
        if 0 <= row < self._rows \
                and 0 <= col < self._cols \
                and self._path[index] == self._matrix[row][col] \
                and not self._visited[row][col]:
            self._visited[row][col] = True
            index += 1
            res = self.hasPathCore(row - 1, col, index) \
                  or self.hasPathCore(row + 1, col, index) \
                  or self.hasPathCore(row, col - 1, index) \
                  or self.hasPathCore(row, col + 1, index)
            if not res:
                index -= 1
                self._visited[row][col] = False
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.hasPath("ABCESFCSADEE", 3, 4, "ABCCED"))
