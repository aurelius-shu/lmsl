# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root.left:
            root.left = root.right
            self.Mirror(root.left)
        if not root.right:
            root.right = root.left
            self.Mirror(root.right)
        if root.left and root.right:
            tmp = root.left
            root.left = root.right
            root.right = tmp
            self.Mirror(root.left)
            self.Mirror(root.right)
