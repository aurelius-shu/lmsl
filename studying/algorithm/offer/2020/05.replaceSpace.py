#-*- coding:utf-8 -*-
"""
    05. 替换空格

    请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

示例 1：
    输入：s = "We are happy."
    输出："We%20are%20happy."

限制：
    0 <= s 的长度 <= 10000

思路：
    使用一个新的列表存储遍历时替换后的结果
"""


class Solution:
    def replaceSpace(self, s: str) -> str:

        if not isinstance(s, str):
            raise ValueError('入参只能是str类型')
        if s is None:
            return None

        news = []
        for c in s:
            if c == ' ':
                news += ['%', '2', '0']
            else:
                news += [c]
        return ''.join(news)
