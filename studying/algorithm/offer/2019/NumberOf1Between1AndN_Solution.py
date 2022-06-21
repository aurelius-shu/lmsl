# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        # 公式：(n/i)*(i/10)+min(max(n%i-i/10+1,0),i/10)
        count1 = 0
        length = len(str(n))
        for i in range(1, length + 1):
            count1 += (n // pow(10, i)) * pow(10, i - 1) + min(
                max(n % (pow(10, i)) - pow(10, i - 1) + 1, 0), pow(10, i - 1))
        return count1


if __name__ == '__main__':
    s = Solution()
    r = s.NumberOf1Between1AndN_Solution(55)
