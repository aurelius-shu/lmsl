# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self._list = []
        self._tmp = []

    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return self._list
        self._tmp.append(root)
        while self._tmp:
            self._list.append(self._tmp[0].val)
            if self._tmp[0].left:
                self._tmp.append(self._tmp[0].left)
            if self._tmp[0].right:
                self._tmp.append(self._tmp[0].right)
            self._tmp.pop(0)
        return self._list
