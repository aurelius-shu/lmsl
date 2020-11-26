# -*- coding:utf-8 -*-

class Solution:
    def NumberOf1(self, n):
        # write code here
        n = (bin(((1 << 32) - 1) & n)[2:]).zfill(32)
        return n.count('1')


if __name__ == '__main__':
    s = Solution()
    print(s.NumberOf1(-1))
