#-*- coding:utf-8 -*-
"""
题目：
    19. 正则表达式匹配
    请实现一个函数用来匹配包含'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。

思路：
动态规划(四种匹配方式)
1. 当 p 下一位是'*'，当前位是'.'，匹配任意长度的任意字符
2. 当 p 下一位是'*'，当前位不是'.'，匹配任意长度当p[i]
3. 当 p 下一位不是'*'，当前位是'.'，匹配单个任意字符
4. 当 p 下一位不是'*'，当前位不是'.'，匹配单个p[i]

注意：
1. 当 s 是空，p 不是空且下一位不是'*'时，直接不成功
"""


class Solution:
    def __init__(self):
        self.d = {}

    def isMatch(self, s: str, p: str) -> bool:
        if (s, p) in self.d:
            return self.d[(s, p)]

        sl, pl = len(s), len(p)

        for i in range(pl):
            if i < pl - 1 and p[i + 1] == '*':
                if p[i] == '.':
                    # 匹配任意字符任意长度
                    res = [self.isMatch(s[i:], p[2:]) for i in range(sl + 1)]
                    if True in set(res):
                        self.d[(s, p)] = True
                        return True
                else:
                    # 匹配任意个p[i]
                    res = {self.isMatch(s, p[2:])}
                    for j in range(sl):
                        if s[j] != p[i]:
                            break
                        res.add(self.isMatch(s[1 + j:], p[2:]))
                    if True in res:
                        self.d[(s, p)] = True
                        return True
            else:
                if p[i] == '.':
                    # 匹配单个任意字符
                    if not s:
                        self.d[(s, p)] = False
                        return False
                    self.d[(s, p)] = self.isMatch(s[1:], p[1:])
                    return self.d[(s, p)]
                else:
                    # 匹配单个 p[i]
                    if s and s[0] == p[i]:
                        self.d[(s, p)] = self.isMatch(s[1:], p[1:])
                        return self.d[(s, p)]
                    self.d[(s, p)] = False
                    return False
        if not s:
            self.d[(s, p)] = True
            return True
        self.d[(s, p)] = False
        return False


s = Solution()
res = s.isMatch('a', '.*..a*')
print(res)
