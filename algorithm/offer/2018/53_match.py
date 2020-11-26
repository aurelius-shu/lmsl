#!/usr/bin/env python3
# -*- coding:utf-8 -*-


'''
53. 正则表达式匹配

实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。 在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配。
'''


def matchcore(s, pattern):
    # 字符串和模式串都运行到了结尾，返回true
    if len(s) == 0 and len(pattern) == 0:
        return True

    # 字符串没到结尾，而模式到了，返回false
    if len(s) != 0 and len(pattern) == 0:
        return False

    # 如果模式串的下一个字符是‘*’，则进入状态机的匹配
    if len(pattern) > 1 and pattern[1] == '*':
        # 如果字符串和模式串相等，或者模式串是‘.’，并且字符串没有到结尾，则继续匹配
        if len(s) > 0 and len(pattern) > 0 and (s[0] == pattern[0] or (pattern[0] == '.' and len(s) != 0)):
            # 进入下一个状态 or 继续‘*’的匹配 or 跳过‘*’
            return matchcore(s[1:], pattern[2:]) or matchcore(s[1:], pattern) or matchcore(s, pattern[2:])
        # 如果字符串和模式串不相等，跳过当前模式串的字符和‘*’，进入新一轮的匹配
        else:
            # 跳过‘*’
            return matchcore(s, pattern[2:])
    # 如果字符串和模式串相等，或者模式串是‘.’，且字符串没有到结尾，则继续匹配
    if len(s) > 0 and len(pattern) > 0 and (s[0] == pattern[0] or(pattern[0] == '.' and len(s) != 0)):
        return matchcore(s[1:], pattern[1:])
    return False


if __name__ == '__main__':
    s = 'aaa'
    pattern = 'ab*ac*a'
    # pattern = 'aa.*a'

    print(matchcore(s, pattern))
