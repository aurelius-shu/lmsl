# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        return self.isSymmetricalCore(pRoot.left, pRoot.right)

    def isSymmetricalCore(self, left, right):
        if not left and not right:
            return True
        if not left or not right or left.val != right.val:
            return False
        return self.isSymmetricalCore(left.left, right.right) and self.isSymmetricalCore(left.right, right.left)
