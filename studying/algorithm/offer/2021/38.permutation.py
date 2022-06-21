class Solution:
    def __init__(self):
        self._s = None
        self._res = []

    def permutation(self, s):
        if not s:
            return self._res
        self._s = s
        self.permutationCore([], list(range(len(s))))
        return list(set(self._res))

    def permutationCore(self, row, indexs):
        if len(indexs) == 1:
            row.append(self._s[indexs[0]])
            self._res.append(''.join(row))
            row.pop()
            return

        for index in indexs:
            row.append(self._s[index])
            self.permutationCore(row, [i for i in indexs if i != index])
            row.pop()
