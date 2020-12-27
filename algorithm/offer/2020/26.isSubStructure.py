#-*- coding:utf-8 -*-
"""
题目：
    26. 树的子结构
    输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

    B是A的子结构， 即 A中有出现和B相同的结构和节点值。

    例如:
    给定的树 A:

         3
        / \
       4   5
      / \
     1   2
    给定的树 B：

       4 
      /
     1
    返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

思路：
先序遍历A，与B做递归比较

注意：

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not B:
            return False

        def isSubStructureCore(ta, tb):
            if not tb:
                return True

            if ta and ta.val == tb.val:
                return isSubStructureCore(ta.left,
                                          tb.left) and isSubStructureCore(
                                              ta.right, tb.right)

            return False

        def checkTreeNode(tree):
            if not tree: return False
            if isSubStructureCore(tree, B): return True
            if checkTreeNode(tree.left): return True
            if checkTreeNode(tree.right): return True
            return False

        return checkTreeNode(A)
