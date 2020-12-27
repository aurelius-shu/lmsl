#-*- coding:utf-8 -*-
"""
题目：
    27. 二叉树的镜像
    请完成一个函数，输入一个二叉树，该函数输出它的镜像。

    例如输入：

         4
       /   \
      2     7
     / \   / \
    1   3 6   9
    镜像输出：

         4
       /   \
      7     2
     / \   / \
    9   6 3   1

思路：
递归交换

注意：
空节点时递归停止
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        root.left, root.right = root.right, root.left
        self.mirrorTree(root.left)
        self.mirrorTree(root.right)
        return root
