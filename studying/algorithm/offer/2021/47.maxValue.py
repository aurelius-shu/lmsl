class Solution:
    def __init__(self):
        self._grid = None
        # 缓存 - 空间换时间
        self._d = {}

    def maxValue(self, grid):
        if not grid or not grid[0]:
            return 0
        m, n = len(grid) - 1, len(grid[0]) - 1
        self._grid = grid
        return self.m(m, n)

    def m(self, m, n):
        if m == 0 and n == 0:
            return self._grid[0][0]
        if m < 0 or n < 0:
            return 0

        # 动态规划
        # f(m,n) = grid[m,n] + max(f(m-1,n), f(m,n-1))
        self._d[(m, n)] = self._grid[m][n] + \
                          max(
                              self._d[(m - 1, n)] if (m - 1, n) in self._d else self.m(m - 1, n),
                              self._d[(m, n - 1)] if (m, n - 1) in self._d else self.m(m, n - 1)
                          )
        return self._d[(m, n)]
