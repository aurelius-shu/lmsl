class Solution:
    def __init__(self):
        self._len = 0
        self._order = []

    def getLeastNumbers(self, arr, k):
        if not k or not arr:
            return []

        self._len = k
        for num in arr:
            self.push(num)
        return self._order

    def push(self, num):
        if self._order and len(self._order) == self._len and num >= self._order[-1]:
            return

        self._order.append(0)
        cursor = len(self._order) - 1
        # 需要前移
        while cursor > 0 and self._order[cursor - 1] > num:
            self._order[cursor] = self._order[cursor - 1]
            cursor -= 1
        # 移不动了
        self._order[cursor] = num
        if len(self._order) > self._len:
            self._order.pop()


if __name__ == '__main__':
    s = Solution()
    res = s.getLeastNumbers([0, 0, 1, 2, 4, 2, 2, 3, 1, 4], 8)
    print(res)
