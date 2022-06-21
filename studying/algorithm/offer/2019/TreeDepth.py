# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        return 0 if not pRoot else 1 + max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right))
