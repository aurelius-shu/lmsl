class Solution:
    def __init__(self):
        self._d = {}

    def firstUniqChar(self, s):
        res = " "
        for c in s:
            self._d[c] = self._d.get(c, 0) + 1
        for c in s:
            if self._d[c] == 1:
                res = c
                break
        return res
