class Solution:
    def numWays(self, n: int) -> int:
        if n < 1:
            return 1
        if n < 2:
            return 1
        if n < 3:
            return 2

        a, b = 1, 2
        while n >= 3:
            a, b = b, a + b
            n -= 1
        return b % 1000000007
