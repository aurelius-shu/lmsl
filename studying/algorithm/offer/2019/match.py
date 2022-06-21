# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if not s and not pattern:
            return True
        # if not s and
        if len(pattern) > 1 and pattern[1] == '*':
            if len(s) > 0 and (s[0] == pattern[0] or pattern[0] == '.'):
                return self.match(s[1:], pattern[2:]) or self.match(s[1:], pattern) or self.match(s, pattern[2:])
            return self.match(s, pattern[2:])
        if len(s) > 0 and len(pattern) > 0:
            if s[0] == pattern[0] or pattern[0] == '.':
                return self.match(s[1:], pattern[1:])
        return False
