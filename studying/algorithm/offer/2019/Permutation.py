# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self._sss = set()

    def Permutation(self, ss):
        # write code here
        ss = [s for s in ss]
        return self.string_permutation(ss, 0)

    def string_permutation(self, ss, index):
        if not ss:
            return self._sss
        if len(ss) == index + 1:
            self._sss.add(''.join([x for x in ss]))

        for i in range(len(ss) - index):
            tmp = ss[index + i]
            ss[index + i] = ss[index]
            ss[index] = tmp

            self.string_permutation(ss, index + 1)

            tmp = ss[index + i]
            ss[index + i] = ss[index]
            ss[index] = tmp

        return list(sorted(self._sss))


if __name__ == '__main__':
    s = Solution()
    sss = s.Permutation("ab")
    for ss in sss:
        print(ss)
