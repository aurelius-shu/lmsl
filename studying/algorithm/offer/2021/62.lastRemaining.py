class Solution:
    def lastRemaining(self, n, m):
        return (self.lastRemaining(n - 1, m) + m) % n if n != 0 else 0
