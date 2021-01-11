#-*- coding:utf-8 -*-
"""
题目：
    20. 表示数值的字符串
    请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"-1E-16"、"0123"都表示数值，但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。

思路：
    配套出现
    底数和指数分开判定

注意：
    set 比较
"""


class Solution:
    def isNumber(self, s: str) -> bool:
        def isExponent(exponent: str):
            if not exponent:
                return False

            if exponent[0] in {'+', '-'}:
                exponent = exponent[1:]

            if not exponent or {
                    c
                    for c in exponent
            } | {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
                 } != {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}:
                return False

            return True

        def isRadix(radix: str):
            if not radix:
                return False

            if radix[0] in {'+', '-'}:
                radix = radix[1:]

            if not radix:
                return False

            if '.' in radix:
                if len(radix.split('.')) != 2:
                    return False
                left, right = radix.split('.')
                if (not left and not right) or {
                        c
                        for c in left
                } | {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'} != {
                        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
                } or {c
                      for c in right} | {
                          '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
                      } != {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}:
                    return False
            else:
                if {c
                        for c in radix
                    } | {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'} != {
                        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
                    }:
                    return False

            return True

        while s and s[0] == ' ':
            s = s[1:]

        while s and s[len(s) - 1] == ' ':
            s = s[:len(s) - 1]

        if not s:
            return False

        s = s.lower()

        if 'e' in s:
            # 科学计数法
            if len(s.split('e')) != 2:
                return False
            radix, exponent = s.split('e')
            if not isExponent(exponent): return False
            if not isRadix(radix): return False
            return True

        else:
            # 非科学计数法
            if not isRadix(s): return False
            return True


s = Solution()
res = s.isNumber('1 ')
print(res)
