# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot or not k:
            return None
        self._k = k
        self._node = None
        self.inOrder(pRoot)
        return self._node

    def inOrder(self, node):
        if not node or self._k <= 0:
            return
        self.inOrder(node.left)
        self._k -= 1
        if self._k == 0:
            self._node = node
        self.inOrder(node.right)
