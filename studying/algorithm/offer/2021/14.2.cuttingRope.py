class Solution:
    def __init__(self):
        self._d = {0: 0, 1: 0, 2: 1, 3: 2, 4: 4, 5: 6, 6: 9}

    def cuttingRope(self, n: int) -> int:
        if n <= 3:
            return self._d[n]

        return self.maxProduct(n) % 1000000007

    def maxProduct(self, n):
        if n in self._d:
            return self._d[n]

        self._d[n] = max([max(
            self.maxProduct(n - i) * i,
            self.maxProduct(n - i) * self.maxProduct(i)
        ) for i in range(1, n)])
        return self._d[n]


if __name__ == '__main__':
    s = Solution()
    print(s.cuttingRope(5))
    print(s._d)
