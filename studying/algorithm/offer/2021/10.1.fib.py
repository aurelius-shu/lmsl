class Solution:

    def __init__(self):
        self._d = {0: 0, 1: 1}

    def fib(self, n: int) -> int:
        res = self.fibCore(n)
        return res // 1000000007

    def fibCore(self, n: int) -> int:
        if n < 0:
            return 0
        if n < 2:
            return self._d[n]

        n2 = self._d[n - 2] if n - 2 in self._d else self.fib(n - 2)
        n1 = self._d[n - 1] if n - 1 in self._d else self.fib(n - 1)

        self._d[n] = n2 + n1
        return self._d[n]
