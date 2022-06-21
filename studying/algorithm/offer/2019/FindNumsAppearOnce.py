# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        diff = 0
        for num in array:
            diff ^= num
        rightBit = self.RightBit(diff)
        num1, num2 = 0, 0
        for num in array:
            if num & rightBit == rightBit:
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]

    def RightBit(self, num):
        if not num:
            return 0
        rightBit = 1
        while num & rightBit != rightBit:
            rightBit = rightBit << 1
        return rightBit


if __name__ == '__main__':
    s = Solution()
    print(s.FindNumsAppearOnce([121, 23, 23, 421, 33, 33]))
