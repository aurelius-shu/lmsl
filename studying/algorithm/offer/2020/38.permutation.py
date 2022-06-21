#-*- coding:utf-8 -*-
"""
题目：
    38. 字符串的排列
    输入一个字符串，打印出该字符串中字符的所有排列。

    你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

    示例:

    输入：s = "abc"
    输出：["abc","acb","bac","bca","cab","cba"]

    限制：

    1 <= s 的长度 <= 8
    
思路：
递归 - 回溯法

注意：
重复字符导致的不同排列也会有重复组合，可以使用set去重
"""


class Solution:
    def permutation(self, s: str):
        def permutation(l):
            res = []
            for c in l:
                copy = l[:]
                copy.remove(c)
                tails = self.permutation(copy)
                if tails:
                    for tail in tails:
                        res.append(c + tail)
                else:
                    res.append(c)
            return res

        return list(set(permutation(list(s))))


if __name__ == "__main__":
    s = Solution()
    res = s.permutation('abc')
    print(res)
