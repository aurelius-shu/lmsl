class Solution:
    def __init__(self):
        self._d = {0: 1}

    def myPow(self, x: float, n: int) -> float:
        reverse = False
        if n < 0:
            reverse = True
            n = 0 - n
        elif n == 0:
            return 1
        elif n == 1:
            return x

        res = (self._d[n // 2] if n // 2 in self._d else self.myPow(x, n // 2)) * \
              (self._d[n - n // 2] if (n - n // 2) in self._d else self.myPow(x, n - n // 2))
        self._d[n] = 1 / res if reverse else res
        return self._d[n]
