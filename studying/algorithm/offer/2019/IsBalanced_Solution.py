# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self._isBalance = True

    def IsBalanced_Solution(self, pRoot):
        # write code here
        self.height(pRoot)
        return self._isBalance

    def height(self, node):
        if not node or not self._isBalance:
            return 0
        left = self.height(node.left)
        right = self.height(node.right)
        if abs(left - right) > 1:
            self._isBalance = False
        return 1 + max(left, right)
