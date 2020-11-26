# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        res = []
        q = [pRoot]
        while q:
            cnt = len(q)
            l = []
            while cnt > 0:
                cnt -= 1
                node = q.pop(0)
                if not node:
                    continue
                l.append(node.val)
                q.append(node.left)
                q.append(node.right)
            if l:
                res.append(l)
        return res
