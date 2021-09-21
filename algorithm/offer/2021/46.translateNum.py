class Solution:
    def __init__(self):
        self._num = ''

    def translateNum(self, num):
        if num is None:
            return 0
        self._num = str(num)
        return self.translate(0, len(str(num)) - 1)

    def translate(self, start, end):
        if start == end:
            return 1

        if start + 1 == end:
            if self._num[start] != '0' and int(self._num[start] + self._num[end]) <= 25:
                return 2
            else:
                return 1

        res1 = self.translate(start + 1, end)
        res2 = self.translate(start + 2, end) \
            if self._num[start] != '0' and int(self._num[start] + self._num[start + 1]) <= 25 \
            else 0
        return res1 + res2
