# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        if not s:
            return 0
        res, isNegative = 0, False
        for i in range(len(s)):
            if i == 0 and s[i] == '-' or s[i] == '+':
                isNegative = (s[i] == '-')
            elif ord(s[i]) < ord('0') or ord(s[i]) > ord('9'):
                return 0
            else:
                res = res * 10 + ord(s[i]) - ord('0')
        if isNegative and res <= 2 ** 31:
            return 0 - res
        if not isNegative and res < 2 ** 31:
            return res
        return 0
