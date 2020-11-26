# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False

        root = sequence[-1]
        i = 0
        left, right = [], []
        while sequence[i] < root:
            left.append(sequence[i])
            i += 1
        while sequence[i] > root:
            right.append(sequence[i])
            i += 1
        if i != (len(sequence) - 1):
            return False

        isLeftBst = True
        if left:
            isLeftBst = self.VerifySquenceOfBST(left)
        isRightBst = True
        if right:
            isRightBst = self.VerifySquenceOfBST(right)
        return isLeftBst and isRightBst
