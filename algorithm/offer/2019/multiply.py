# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        B = []
        product = 1
        for i in range(len(A)):
            B.append(product)
            product *= A[i]
        product = 1
        for i in range(len(A) - 1, -1, -1):
            B[i] *= product
            product *= A[i]
        return B
