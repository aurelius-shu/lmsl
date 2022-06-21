#-*- coding:utf-8 -*-
"""
题目：
    32 - I. 从上到下打印二叉树
    从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

    例如:
    给定二叉树: [3,9,20,null,null,15,7],

     3
    / \
    9  20
       /  \
      15   7
    
    返回：
    [3,9,20,15,7]

思路：
    挨层处理，队列记录每一层，
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        queue, res = [], []
        queue.append(root)
        while queue:
            cur = queue.pop(0)
            queue.append(cur.left)
            queue.append(cur.right)
            res.append(cur.val)
        return res
