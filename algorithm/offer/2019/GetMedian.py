# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self._left = []
        self._right = []
        self._n = 0

    def Insert(self, num):
        # write code here
        if self._n % 2 == 0:
            self._left.append(num)
            self._left.sort(reverse=True)
            self._right.append(self._left.pop(0))
            self._right.sort()
        else:
            self._right.append(num)
            self._right.sort()
            self._left.append(self._right.pop(0))
            self._left.sort(reverse=True)
        self._n += 1

    def GetMedian(self, num):
        # write code here
        self.Insert(num)
        if self._n % 2 == 1:
            return round(float(self._right[0]), 2)
        else:
            return round((self._left[0] + self._right[0]) / 2.0, 2)


if __name__ == '__main__':
    s = Solution()
    l = [5, 2, 3, 4, 1, 6, 7, 0, 8]
    for i in l:
        print(s.GetMedian(i))
