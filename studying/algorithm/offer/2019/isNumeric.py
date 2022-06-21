# -*- coding:utf-8 -*-

import re


class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if not s:
            return False
        return not not re.match(r'^[+-]?\d*(\.\d+)?([Ee][+-]?\d+)?$', s)
