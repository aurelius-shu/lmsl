#-*- coding:utf-8 -*-
"""
    07. 重建二叉树

    输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

例如，给出

    前序遍历 preorder = [3,9,20,15,7]
    中序遍历 inorder = [9,3,15,20,7]
    返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

限制：
    0 <= 节点个数 <= 5000

思路：
    子树的根节点在前序遍历中是第一个，在中序遍历中是左右子树的切分点
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        if not (isinstance(preorder, list) and isinstance(inorder, list)):
            return None

        if not preorder:
            return None

        if len(preorder) == 1:
            return TreeNode(preorder[0])

        root = TreeNode(preorder[0])
        split_index = inorder.index(root.val)
        inorder_left, inorder_right = inorder[0:split_index], inorder[
            split_index + 1:]
        preorder_left, preorder_right = preorder[1:split_index +
                                                 1], preorder[split_index + 1:]
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)
        return root