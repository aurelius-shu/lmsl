# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return None
        if pNode.right:
            node = pNode.right
            while node.left:
                node = node.left
            return node
        else:
            while pNode.next:
                node = pNode.next
                if node.left == pNode:
                    return node
                pNode = node
            return None
