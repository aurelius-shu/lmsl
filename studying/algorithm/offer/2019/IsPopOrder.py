# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self._data = []

    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV or not popV:
            return False
        if len(popV) != len(pushV):
            return False

        while pushV:
            self._data.append(pushV.pop(0))
            while self._data and self._data[-1] == popV[0]:
                self._data.pop()
                popV.pop(0)
        return (not popV)


if __name__ == '__main__':
    s = Solution()
    pushV = [1, 2, 3, 4, 5]
    popV = [4, 5, 3, 2, 1]
    s.IsPopOrder(pushV, popV)
