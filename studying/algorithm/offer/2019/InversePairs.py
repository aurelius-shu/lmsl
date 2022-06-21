# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self._cnt = 0

    def InversePairs(self, data):
        # write code here
        self._data = data
        self._tmp = [0] * len(data)
        self.mergeSort(0, len(data) - 1)
        return self._cnt % 1000000007

    def mergeSort(self, start, end):
        if start >= end:
            return
        mid = (end + start) // 2
        self.mergeSort(start, mid)
        self.mergeSort(mid + 1, end)
        self.merge(start, mid, end)

    def merge(self, start, mid, end):
        i, j, k = start, mid + 1, start
        while i <= mid or j <= end:
            if i > mid:
                self._tmp[k] = self._data[j]
                j += 1
            elif j > end:
                self._tmp[k] = self._data[i]
                i += 1
            elif self._data[i] <= self._data[j]:
                self._tmp[k] = self._data[i]
                i += 1
            else:
                self._tmp[k] = self._data[j]
                j += 1
                self._cnt += (mid - i + 1)
            k += 1
        for i in range(end - start + 1):
            self._data[i + start] = self._tmp[i + start]


if __name__ == '__main__':
    s = Solution()
    print(s.InversePairs([7, 5, 6, 4]))
