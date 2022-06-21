# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        return self.convertCore(pRootOfTree, False)

    def convertCore(self, node, isSmaller):
        if not node:
            return
        if not node.left and not node.right:
            return node
        left = self.convertCore(node.left, True) if node.left else None
        right = self.convertCore(node.right, False) if node.right else None
        node.left = left
        if left: left.right = node
        node.right = right
        if right: right.left = node

        if isSmaller:
            while node.right:
                node = node.right
        else:
            while node.left:
                node = node.left
        return node
