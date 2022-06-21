class Solution:

    def __init__(self):
        self._row_counts = 0
        self._col_counts = 0
        self._m = None
        self.k = 0
        self.count = 0

    def movingCount(self, m: int, n: int, k: int) -> int:
        if m < 1 or n < 1:
            return 0

        self._row_counts, self._col_counts, self.k = m, n, k
        self._m = [[1 for i in range(n)] for j in range(m)]
        self.moving(0, 0)
        return self.count

    def moving(self, i, j):
        if i < 0 or i >= self._row_counts or j < 0 or j >= self._col_counts:
            return
        if self.digitCount(i, j) <= self.k and self._m[i][j] == 1:
            self._m[i][j] = 0
            self.count += 1
            self.moving(i - 1, j)
            self.moving(i + 1, j)
            self.moving(i, j - 1)
            self.moving(i, j + 1)

    @staticmethod
    def digitCount(i, j):

        count = 0
        ij = str(i) + str(j)
        for n in ij:
            count += int(n)
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.movingCount(11, 8, 16))
