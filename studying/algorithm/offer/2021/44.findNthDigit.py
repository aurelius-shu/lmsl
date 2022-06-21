class Solution:
    def __init__(self):
        self._d = {1: 9}

    def findNthDigit(self, n):

        if n < 10:
            return n

        digit = 1
        # 找到会超出 第 n 个数位所表示数的数字位数
        while self.f(digit) <= n:
            digit += 1

        num = self.f(digit - 1)
        # 若刚好是上个数字位数表示的最后一个数位，直接返回 9
        if n == num:
            return 9

        # n 所在数字的值
        val = 10 ** (digit - 1) + (n - num - 1) // digit
        # n 在 val 中的索引位置
        return int(str(val)[(n - num - 1) % digit])

    def f(self, digit):
        if digit == 1:
            return 9
        self._d[digit] = (self._d[digit - 1] \
                              if (digit - 1) in self._d \
                              else self.f(digit - 1)) + \
                         (digit * 9 * 10 ** (digit - 1))
        return self._d[digit]


if __name__ == '__main__':
    s = Solution()
    res = s.findNthDigit(1000)
    print(res)
